import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

import app  # noqa: E402


class TestStudentApp(unittest.TestCase):
    def test_default_student_information(self):
        for key in ("STUDENT_NAME", "STUDENT_SURNAME", "STUDENT_GROUP", "STUDENT_ID"):
            os.environ.pop(key, None)
        banner = app.build_banner(app.get_student())
        self.assertIn("Name: Zakariya", banner)
        self.assertIn("Surname: Polevchshikov", banner)
        self.assertIn("Group: IT2-2312", banner)
        self.assertIn("Student ID: 37052", banner)
        self.assertIn("Application is running successfully!", banner)

    def test_environment_variables_are_used(self):
        os.environ["STUDENT_GROUP"] = "TEST-GROUP"
        try:
            banner = app.build_banner(app.get_student())
            self.assertIn("Group: TEST-GROUP", banner)
        finally:
            del os.environ["STUDENT_GROUP"]


if __name__ == "__main__":
    unittest.main()
