a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [val for val in a if val % 2 == 0]
print(res)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(filter(lambda val: val % 2 == 0, a))
print(res)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in a:
    if val % 2 == 0:
        print(val, end=" ")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [val for val in a if val & 1 == 0]
print(res)

