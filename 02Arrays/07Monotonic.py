# Check if given array is Monotonic
def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False


# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))

# Python Program to check if given array is Monotonic
# Check if given array is Monotonic

def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))

def isMonotonic(arr):
    if len(arr) <= 2:
        return True
    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i - 1]
            continue
        if (direction > 0 and arr[i] < arr[i - 1]) or (direction < 0 and arr[i] > arr[i - 1]):
            return False
    return True


# Example usage
arr1 = [1, 2, 3, 4, 5]  # True
arr2 = [5, 4, 3, 2, 1]  # True
arr3 = [1, 2, 2, 3, 4]  # True
arr4 = [1, 2, 3, 4, 5, 4]  # False

print(isMonotonic(arr1))  # should return True
print(isMonotonic(arr2))  # should return True
print(isMonotonic(arr3))  # should return True
print(isMonotonic(arr4))  # should return False