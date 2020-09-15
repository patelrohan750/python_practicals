#E).Develop a python program to sort five integer values
numbers=[]
print("Enter The Numbers\n")
for i in range(5):
    number=int(input())
    numbers.append(number)
print(numbers)
numbers.sort()
print(f"sorted number is {numbers}")
