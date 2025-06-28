s = 1
e = 10

for i in range(s, e + 1):
    if i % 2 == 0:
        print(i)

s = 1
e = 10

res = [i for i in range(s, e + 1) if i % 2 == 0]
print(res)

s = 1
e = 10

for i in range(2, e + 1, 2):
    print(i)