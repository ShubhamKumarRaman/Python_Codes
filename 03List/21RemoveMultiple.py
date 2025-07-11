a = [10, 20, 30, 40, 50, 60, 70]

# Elements to remove
remove = [20, 40, 60]

# Remove elements using a simple for loop
res = []

for val in a:
    if val not in remove:
        res.append(val)

print(res)


a = [10, 20, 30, 40, 50, 60, 70]

# Elements to remove
remove = [20, 40, 60]

# Remove elements using list comprehension
a = [x for x in a if x not in remove]

print(a)

a = [10, 20, 30, 40, 50, 60, 70]

# Elements to remove
remove = [20, 40, 60]

# Remove elements using remove() in a loop
for val in remove:
    while val in a:
        a.remove(val)

print(a)

a = [10, 20, 30, 40, 50, 60, 70]

# Elements to remove
remove = {20, 40, 60}

# Remove elements using filter
a = list(filter(lambda x: x not in remove, a))

print(a)