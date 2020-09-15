#C.write a python program to demonstrate constructors
class Addition:
    first_number = 0
    second_number = 0
    result = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first_number = f
        self.second_number = s

    def calculate(self):
        self.answer = self.first_number + self.second_number

    def display(self):
        print(f"First number is {self.first_number} ")
        print(f"Second number is {self.second_number}")
        print(f"Addition of two numbers is {self.answer}")

num1=int(input("Enter Fisrt Number: "))
num2=int(input("Enter second Number: "))
obj = Addition(num1,num2)
obj.calculate()
obj.display()

