pipeline {
    agent any

    environment {
        STUDENT_NAME    = 'Zakariya'
        STUDENT_SURNAME = 'Polevchshikov'
        STUDENT_GROUP   = 'IT2-2312'
        STUDENT_ID      = '37052'

        IMAGE_NAME      = 'polevchshikov-zakariya-devops'
        CONTAINER_NAME  = 'polevchshikov-zakariya-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh '''
                    echo "Git commit used by Jenkins:"
                    git log -1 --pretty=format:"%H %an %s%n"
                    ls -la
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "Checking Bash script syntax..."
                    bash -n scripts/Polevchshikov_Zakariya_system.sh
                    chmod +x scripts/Polevchshikov_Zakariya_system.sh
                    ./scripts/Polevchshikov_Zakariya_system.sh

                    echo "Compiling Python application..."
                    python3 -m py_compile app/app.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "Checking required project files..."
                    for f in Polevchshikov_Zakariya_info.txt config/app.conf Dockerfile docker-compose.yml .gitignore; do
                        test -f "$f" && echo "OK: $f" || { echo "MISSING: $f"; exit 1; }
                    done
                    grep -q "Student ID: 37052" Polevchshikov_Zakariya_info.txt

                    echo "Running unit tests..."
                    python3 -m unittest discover -s tests -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest .
                    docker images ${IMAGE_NAME}
                '''
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} 2>/dev/null || true
                    docker run -d \
                        -e STUDENT_NAME=${STUDENT_NAME} \
                        -e STUDENT_SURNAME=${STUDENT_SURNAME} \
                        -e STUDENT_GROUP=${STUDENT_GROUP} \
                        -e STUDENT_ID=${STUDENT_ID} \
                        -p 8000:8000 \
                        --name ${CONTAINER_NAME} \
                        ${IMAGE_NAME}:latest
                    sleep 3
                    docker ps --filter name=${CONTAINER_NAME}
                    echo "Container logs:"
                    docker logs ${CONTAINER_NAME}
                    docker logs ${CONTAINER_NAME} | grep -q "Application is running successfully!"
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline for ${STUDENT_NAME} ${STUDENT_SURNAME} (${STUDENT_GROUP}, ID ${STUDENT_ID}) finished successfully."
        }
        failure {
            echo 'Pipeline failed. Check the stage that is marked red.'
        }
    }
}
