# E.To find all prime numbers within a given range.
a = int(input("Enter lower range: "))
b = int(input("Enter upper range: "))

for num in range(a, b + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
