#c).to write a python program for linear search
def linearSearch(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            print(f"{item} Found in Index {i+1}")
arr=[]
arr_size=int(input("Enter The Size Of the Array: "))
for i in range(arr_size):
    arr_element=int(input("Enter The The Elemnt At "+str(i+1)+" : "))
    arr.append(arr_element)
item=int(input("Enter Element You Want To Search: "))
linearSearch(arr,item)
