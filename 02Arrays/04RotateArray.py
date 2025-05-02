# Function to reverse arr[]
def rverseArray(arr,d):
    c=(arr[d:])+(arr[:d])
    return c
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
d=2
print(rverseArray(arr,d))

# Python program for reversal algorithm of array rotation
 
# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)
 # Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i])
 # Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2) # Rotate array by 2
printArray(arr)

# Python program for reversal algorithm of array rotation
 
# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)
 # Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i])
 # Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2) # Rotate array by 2
printArray(arr)

from collections import deque

def rotate_array_deque(arr, d):
    n = len(arr)
    rotated_array = deque(arr)
    rotated_array.rotate(-d)
    return list(rotated_array)

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

rotated_array = rotate_array_deque(arr, d)
print("Rotated array:", rotated_array)