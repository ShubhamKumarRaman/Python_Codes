# Initialize a list
my_list = [1, 2, 3, 4, 5]

# Interchange first and last elements
my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the modified list
print("List after swapping first and last elements:", my_list)

# Swap function
def swapList(newList):
    size = len(newList)
    
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

# Swap function
def swapList(list):
    
    # Storing the first and last element 
    # as a pair in a tuple variable get
    get = list[-1], list[0]
    
    # unpacking those elements
    list[0], list[-1] = get
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

def swap_first_last_3(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst

# Initializing the input
inp=[12, 35, 9, 56, 24]

# Printing the original input
print("The original input is:",inp)

result=swap_first_last_3(inp)

# Printing the result
print("The output after swap first and last is:",result)