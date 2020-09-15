# to write a python program to create,slice,change,delete,and indexing elemnts using tuple

print("1.create")
print("2.slice")
print("3.change")
print("4.delete")
print("5.index")
print("6.display")
print("7.Exit")
user_choice = ''
tuple1 = ()
while user_choice != 7:

    user_choice = int(input("select the choice:\n "))
    if user_choice == 1:
        elemnts_number = int(input("How many elemnts you want to Enter\n"))
        elemnts = print("enter The Elemnts:")
        for i in range(elemnts_number):
            ele = input()
            tuple1 = tuple1 + (ele,)
        print("tuple is: ", tuple1)
    elif user_choice == 2:
        start_point = int(input("Enter The Starting point: "))
        End_point = int(input("Enter The Ending point: "))
        if start_point == 0 and End_point == 0:
            print(tuple1[:])
        elif start_point == 0:
            print(tuple1[:End_point])
        elif End_point == 0:
            print(tuple1[start_point:])
        else:
            print(tuple1[start_point:End_point])

    elif user_choice == 3:
        print(
            "tuples are immutable.\nThis means that elements of a tuple cannot be changed once they have been assigned. ")

    elif user_choice == 4:
        print("Tuple are immutable\n")
    elif user_choice == 5:
        tuple_index = int(input("Enter index: "))
        print(tuple1[tuple_index])
    elif user_choice == 6:
        print(tuple1)
    elif user_choice == 7:
        exit()
    else:
        print("you Enter Wrong Choice...")
