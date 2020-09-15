# D.write a python program to compute the GCD of two numbers

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

i = 1
while i <= num1 and i <= num2:
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i = i + 1
print(f"GCD is {gcd}")
