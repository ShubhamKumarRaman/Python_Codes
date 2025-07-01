a = [-10, 15, 0, 20, -5, 30, -2]

# Using a for loop to print positive number
for val in a:
    if val > 0:
        print(val)

a = [-10, 15, 0, 20, -5, 30, -2]

# List comprehension to filter positive numbers
res = [i for i in a if i > 0]
print(res)

a = [-10, 15, 0, 20, -5, 30, -2]

# Using filter() to get positive numbers
res = filter(lambda x: x > 0, a)

# Convert filter object to list and print
print(list(res))