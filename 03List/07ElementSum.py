a = [10, 20, 30, 40, 50]
res = sum(a)
print(res)

# Using Loop
a = [10, 20, 30, 40, 50]
res = 0  # Initialize sum variable

for i in a:
    res += i
print(res)

# Using list comprehension
a = [10, 20, 30, 40, 50]

res = sum([i for i in a])
print(res)
