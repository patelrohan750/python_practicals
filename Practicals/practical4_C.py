# c)Develop python to sort python Dictnories by key or value
d = {"A": 1, "C": 5, "D": 2, "M": 20, "E": 3, "B": 4}
print("sorted Key is: ")
for i in sorted(d.keys()):
    print(i, end=" ")
print("\nsorted value is: ")
for j in sorted(d.values()):
    print(j, end=" ")
