a = [5, -3, 7, -1, 2, -9, 4]

# Loop through the list and print negative numbers
for num in a:
    if num < 0:
        print(num)

a = [5, -3, 7, -1, 2, -9, 4]

# Using list comprehension to filter negative numbers
n = [num for num in a if num < 0]

print(n)

# Using Filter function
a = [5, -3, 7, -1, 2, -9, 4]

# Using filter function to find negative numbers
n = list(filter(lambda x: x < 0, a))
print(n)

# Using map function
a = [5, -3, 7, -1, 2, -9, 4]

# Using map to filter negative numbers
n = list(map(lambda x: x if x < 0 else None, a))

# Removing None values and printing negative numbers
n = [num for num in n if num is not None]
print(n)