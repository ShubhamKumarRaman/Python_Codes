# Using len()
a = [1, 2, 3, 4, 5]
print(len(a))

# Using loop (Naive method)
a = [1, 2, 3, 4, 5]
c = 0

for val in a:
    c += 1

print(c)

# Using length_hint() from operator Module
from operator import length_hint

a = [1, 2, 3, 4, 5]

print(length_hint(a))