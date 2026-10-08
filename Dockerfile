# Base image: a small official Python image
FROM python:3.12-slim

# Metadata about the image author
LABEL maintainer="Zakariya Polevchshikov <IT2-2312, ID 37052>"

# Default student information (can be overridden with docker run -e ...)
ENV STUDENT_NAME=Zakariya \
    STUDENT_SURNAME=Polevchshikov \
    STUDENT_GROUP=IT2-2312 \
    STUDENT_ID=37052 \
    APP_PORT=8000 \
    PYTHONUNBUFFERED=1

# All following commands run inside /app in the container
WORKDIR /app

# Copy the application, config and student info file into the image
COPY app/ ./app/
COPY config/app.conf ./config/app.conf
COPY Polevchshikov_Zakariya_info.txt .

# Check the code compiles and create a non-root user to run the app
RUN python -m py_compile app/app.py \
    && useradd --create-home appuser

USER appuser

# The application listens on port 8000
EXPOSE 8000

# Command executed when the container starts
CMD ["python", "app/app.py"]
