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