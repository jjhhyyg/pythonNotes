import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """
    - 雇员方法的测试类
    """

    def setUp(self):
        """
        - 创建测试用的雇员类
        :return: None
        """
        self.employee = Employee('Eriksson', 'Hou', 200000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 205000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 210000)


if __name__ == '__main__':
    unittest.main()
