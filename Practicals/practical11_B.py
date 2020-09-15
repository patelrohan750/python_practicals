# B.write a python program to demonstrate class method or static method
from datetime import date as dt
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def isAdult(age):
        if age > 18:
            print(age)
            return True
        else:
            print(age)
            return False
    @classmethod
    def emp_from_year(emp_class, name, year):
        return emp_class(name, dt.today().year - year)
    def __str__(self):
        return f"Employee Name: {self.name} and Age: {self.age}"
e1 = Employee('bruce', 15)
print(e1)
e2 = Employee.emp_from_year('wayne', 1987)
print(e2)
print(Employee.isAdult(e1.age))
print(Employee.isAdult(e2.age))
