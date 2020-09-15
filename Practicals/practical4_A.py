#A).Develop a python program to find largest Element in Array
array = [10, 65, 47, 85, 63, 21, 45, 95]
# max_element=max(array)
# print(f"Largest Element in Array: {max_element}")

max_element = array[0]
for i in range(0, len(array)):
    if array[i] > max_element:
        max_element = array[i]
print(f"Largest Element in Array: {max_element}")
