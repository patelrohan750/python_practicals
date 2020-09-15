#B). to write a python program to change,delete,add,and remove elemnts in dictonary
d = {26: "rohan", 24: "rahul"}
user_choice = ''
while user_choice != 'q':
    print("Enter Your Choice You Want To Do")
    print("1.Add")
    print("2.change")
    print("3.delete")
    print("4.remove")
    print("If You Want to Quit Press 'q ")
    user_choice = input()
    if user_choice == '1':
        d_key = input("Enter Dictonary Key: ")
        d_value = input("Enter Dictonary Value: ")
        d[d_key] = d_value
        print(d)
    elif user_choice == '2':
        print("What you Want to change it.")
        d_key = input("Enter Dictonary Key: ")
        if d_key in d:
            d_value = input("Enter Dictonary Value you want to change: ")
            d[d_key] = d_value
            print(d)
        else:
            print("Your Key is not in Dictonary")
    elif user_choice=='3':
        print("What you Want to Delete it.")
        d_key = input("Enter Dictonary Key: ")
        if d_key in d:
            del d[d_key]
            print(d)
        else:
            print("Your Key is not in Dictonary")

    elif user_choice=='4':
        print("What you Want to remove it.")
        d_key = input("Enter Dictonary Key: ")
        print(d.pop(d_key,'not found key '))
        print(d)
    elif user_choice=='q':
        exit()
    else:
        print("You Enter Wrong Input Please select Correct Input")






