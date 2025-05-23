a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list
if 30 in a:
    print("Element exists in the list")
else:
    print("Element does not exist")


a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list using a loop
key = 30
flag = False

for val in a:
    if val == key:
        flag = True
        break

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")

# Using any()
a = [10, 20, 30, 40, 50]

# Check if 30 exists using any() function
flag = any(x == 30 for x in a)

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")
