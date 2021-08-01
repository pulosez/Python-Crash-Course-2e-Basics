import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('John', 'Connor', 80_000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 85_000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10_000)
        self.assertEqual(self.employee.salary, 90_000)


if __name__ == '__main__':
    unittest.main()
