# A).To implement stack using list

def push(stk, element):
    stk.append(element)


def pop(stk):
    if stk == []:
        return -1
    else:
        return stk.pop()


def peep(stk):
    n = len(stk)
    return stk[n - 1]


def display(stk):
    return stk


user_choice = ''
stk = []
while user_choice != 5:
    print("1.Push")
    print("2.Pop")
    print("3.peep")
    print("4.Display")
    print("5.Exit")
    user_choice = int(input("Enter Your Choice: "))
    if user_choice == 1:
        element = input("Enter stack Element: ")
        push(stk, element)
    elif user_choice == 2:
        pop_element = pop(stk)
        if pop_element == -1:
            print("Your Stack Is Empty!!!")
        else:
            print(f"Deleted element is {pop_element}")
    elif user_choice == 3:
        print(f"Top Element in Stack {peep(stk)}")
    elif user_choice == 4:
        print(display(stk))
    elif user_choice == 5:
        exit()
    else:
        print("Invalid Input!!!")
