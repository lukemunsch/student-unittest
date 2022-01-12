import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student('Steve', 'Rogers')

        self.assertEqual(student.full_name, 'Steve Rogers')
        
    def test_alert_santa(self):
        student = Student('Wade', 'Wilson')
        student.alert_santa()

        self.assertTrue(student.naughty_list)



if __name__ == "__main__":
    unittest.main()
