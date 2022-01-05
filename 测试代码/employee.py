class Employee:
    """
    - 存储雇员基本信息（名、姓和年薪）的类
    """

    def __init__(self, first, last, annual_salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = annual_salary

    def give_raise(self, additional_annual_salary=5000):
        """
        增加雇员年薪
        :param additional_annual_salary: 增加的年薪，默认为5000美元
        :return: None
        """
        self.annual_salary += additional_annual_salary
