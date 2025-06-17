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