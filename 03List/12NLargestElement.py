# Python program to find N largest
# element from given list of integers

# Function returns N largest elements


def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]

        list1.remove(max1)
        final_list.append(max1)

    print(final_list)


# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(list1, N)

# Python program to find N largest
# element from given list of integers

l = [1000,298,3579,100,200,-45,900]
n = 4

l.sort()
arr = []

while n:
    arr.append(l[-n])
    n -= 1
    
print(arr)

import heapq


def find_n_largest_elements(lst, N):
    heap = lst
    return heapq.nlargest(N, heap)


# Test the function with given inputs
lst = [4, 5, 1, 2, 9]
N = 2
print(find_n_largest_elements(lst, N))

lst = [81, 52, 45, 10, 3, 2, 96]
N = 3
print(find_n_largest_elements(lst, N))


import numpy as np

def Nmaxelements(list1, N):
    list1 = np.array(list1) # convert list to numpy array
    return list1[np.argsort(list1)[-N:]]

list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 3
print(Nmaxelements(list1, N))

# python program to find n largest elements in the given list
# Initializing the list
list = [2, 1, 8, 7, 3, 0, 9, 4]
n = 3
res = []
list1 = []

# printing the original list
print('The given list is:', list)

# using sorted()
list1 = sorted(list, reverse=True)
for i in range(0, n):
    res.append(list1[i])

# list after sorting
print('The sorted list is:', list1)

# printing the n largest elements in the list
print('The ', n, ' largest elements in the given list are:', res)

