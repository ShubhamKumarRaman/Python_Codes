a = [[1, 2], [], [3, 4], [], [5]]
res = []

# Iterate over list 'a'
for b in a:
  
    # If list is not empty then add it to res.
    if b:
        res.append(b)

print(res)

a = [[1, 2], [], [3, 4], [], [5]]
res = [b for b in a if b]

print(res)

a = [[1, 2], [], [3, 4], [], [5]]

res = list(filter(lambda b: b, a))

# By using None as the first parameter in filter,
# it removes any falsy values (like empty list)

# res = list(filter(None, a)) # This will also work

print(res)

