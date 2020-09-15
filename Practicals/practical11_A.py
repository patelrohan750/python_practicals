#A.write a python program to demonstrate working of classes and objects

class Student:
    def __init__(self,name,roll,branch,clg):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.clg=clg
    def Display_Details(self):
        print("Student Details:")
        print("Student Name:", self.name)
        print("Student RollNo:", self.roll)
        print("Student Branch:", self.branch)
        print("Student college:", self.clg)

s=Student("Rohan",26,"computer","sk")
s.Display_Details()
print("------------------------------------------------------")
s1=Student("xyz",32,"Ce","sk")
s1.Display_Details()
