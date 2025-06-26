a = [10, 15, 23, 42, 37, 51, 62, 5]

for i in a:
    if i % 2 != 0:
        print(i)

a = [10, 15, 23, 42, 37, 51, 62, 5]

res = [i for i in a if i % 2 != 0]

print(res)

a = [10, 15, 23, 42, 37, 51, 62, 5]

res = filter(lambda x: x % 2 != 0, a)

print(list(res))