# B).to write a python program for tower of hanoi scenario.
def hanoi(disk, source, auxiliary, target):
    if disk == 1:
        print("move disk 1 from {} to {}".format(source, target))
        return
    hanoi(disk - 1, source, target, auxiliary)
    print("move disk {} from {} to {}".format(disk, source, target))
    hanoi(disk - 1, auxiliary, source, target)


disk = int(input("Enter Number of Disk:"))
hanoi(disk, 'A', 'B', 'C')
