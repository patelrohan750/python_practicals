# C.To write a program to find given number is Armstrong or not.

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3

    temp = temp // 10

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
