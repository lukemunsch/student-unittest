import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.student = Student('Peter', 'Parker')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'Peter Parker')

    def test_email_address(self):
        print('test email_address')
        self.assertEqual(self.student.email_address, 'peter.parker@email.com')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


if __name__ == "__main__":
    unittest.main()
