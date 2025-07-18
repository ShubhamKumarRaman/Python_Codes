start, end = -5, 0  
for i in range(start, end + 1):  
    if i < 0:  # Check if the number is negative
        print(i)

start, end = -10, 0
# List comprehension to generate a list of negative numbers within the range
n = [i for i in range(start, end + 1) if i < 0]  
print(n)

start, end = -10, 0 

# Use filter() to keep only  negative numbers from  range and convert result to a list
n = list(filter(lambda x: x < 0, range(start, end + 1)))  

print(n)

start, end = -10, 0  
n = list(map(lambda x: x if x < 0 else None, range(start, end + 1)))  

# Use list comprehension to remove None values (non-negative numbers)
n = [num for num in n if num is not None]  
print(n)