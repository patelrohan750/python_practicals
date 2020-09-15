# F. To print ‘n terms of Fibonacci series using iteration.


num = int(input("Enter number: "))
a, b = 0, 1
while b < num:
    print(b)
    a, b = b, a + b
