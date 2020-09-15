# A)to read and write from file
with open("file1.txt", "r+") as f:
    read = f.readlines()
    for r in read:
        print(r)

    write = f.write("this is write mode\n")
print(".......................done................")
