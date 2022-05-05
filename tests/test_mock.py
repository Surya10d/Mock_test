import unittest
from unittest import mock
from lib.log_application import LogApplication


class Testmock(unittest.TestCase):

    def test_lower(self):
        self.assertEqual("testing", ("TESTING".lower()), msg="Assertion equal is checked")

    def test_upper(self):
        a = "testing".upper()
        self.assertEqual("TESTING", a, msg="Assertion equal is checked")

    def test_numeric(self):
        self.assertTrue(int("12345"), msg="Assertion True is checked")

    def test_true(self):
        a = "true"
        self.assertTrue(a, msg="Assertion True is checked")

    def test_false(self):
        a = ""
        self.assertFalse(a, msg="Assertion False is checked")

    def test_write_log_message_without_using_mock(self):
        value = LogApplication().write_log_message("mock test")
        self.assertEqual(value, "Log message is wrote successfully")

    @mock.patch("lib.log_application.LogApplication.write_log_message", return_value="Mock_response")
    def test_write_log_message_using_mock_first_method(self, mock_response):
        self.assertEqual(LogApplication.write_log_message("mock"), "Mock_response")

    def test_write_log_message_using_mock_second_method(self):
        with mock.patch("lib.log_application.LogApplication.write_log_message", return_value="Mock_response"):
            self.assertEqual(LogApplication.write_log_message("mock"), "Mock_response")


if __name__ == "__main__":
    unittest.main()
