#D).to write a python program for binary search
def binarySearch(arr,item):
    first=0
    last=len(arr)-1
    while first<=last:
        mid = (first + last) // 2
        if item==arr[mid]:
            return mid
        if item>arr[mid]:
            first=mid+1
        else:
            last=mid-1
    else:
        return False
arr=[]
arr_size=int(input("Enter The Size Of the Array: "))
for i in range(arr_size):
    arr_element=int(input("Enter The The Element in Acceding order At "+str(i+1)+" : "))
    arr.append(arr_element)

item=int(input("Enter Element You Want To Search: "))
result=binarySearch(arr,item)
if result:
    print(f"Element Found In {result+1}")
else:
    print("Element is not Found")
