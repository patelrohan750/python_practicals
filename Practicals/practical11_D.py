#D. write a python program to demonstrate inheritance

class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def Dispaly_Emp_Details(self):
        print(f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}")

class Programmer(Employee):

    def __init__(self, name, salary, role, languages):
        super().__init__(name,salary,role)
        self.languages = languages


    def Display_Pro_Deatails(self):
         print(f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}."
               f"The languages are {self.languages}")

p1=Programmer("rohan",20000,"Developer","python")
p1.Display_Pro_Deatails()
