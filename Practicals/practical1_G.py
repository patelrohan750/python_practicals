# G. Write a program to print following pattern:
# A
# B C
# D E F
# G H I J
# K L M N O

ch='A'

for i in range(0,6):
    for j in range(i):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
