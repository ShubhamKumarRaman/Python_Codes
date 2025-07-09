start, end = -5, 0  
for i in range(start, end + 1):  
    if i < 0:  # Check if the number is negative
        print(i)

start, end = -10, 0
# List comprehension to generate a list of negative numbers within the range
n = [i for i in range(start, end + 1) if i < 0]  
print(n)

