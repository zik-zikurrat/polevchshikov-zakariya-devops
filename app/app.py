"""DevOps student application.

Prints the student's information and then serves the same information
over HTTP. Values are read from environment variables, so they can be
changed with `docker run -e ...`, docker-compose or Jenkins without
rebuilding the image.
"""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

LINE = "=" * 32


def get_student():
    """Read student information from environment variables (with defaults)."""
    return {
        "name": os.environ.get("STUDENT_NAME", "Zakariya"),
        "surname": os.environ.get("STUDENT_SURNAME", "Polevchshikov"),
        "group": os.environ.get("STUDENT_GROUP", "IT2-2312"),
        "student_id": os.environ.get("STUDENT_ID", "37052"),
    }


def build_banner(student):
    """Return the text that the application displays."""
    return "\n".join([
        LINE,
        "DevOps Student Application",
        LINE,
        "",
        f"Name: {student['name']}",
        f"Surname: {student['surname']}",
        f"Group: {student['group']}",
        f"Student ID: {student['student_id']}",
        "",
        "Application is running successfully!",
    ])


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = "OK\n"
        else:
            body = build_banner(get_student()) + "\n"
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    print(build_banner(get_student()), flush=True)
    port = int(os.environ.get("APP_PORT", "8000"))
    print(f"\nListening on port {port} (open http://localhost:{port})", flush=True)
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
