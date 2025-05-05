# Python program to split array and move first
# part to end.


def splitArr(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]

		arr[n-1] = x


# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
	print(arr[i], end=' ')

# Code Contributed by Mohit Gupta_OMG <(0_o)>


# Python program to split array and move first
# part to end.


def splitArr(a, n, k):
	b = a[:k]
	return (a[k::]+b[::])


# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
	print(arr[i], end=' ')


# Python program to split array and move first
# part to end.

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
	print(i, end=" ")


def split_and_add(arr, n):
	return [arr[(i + n) % len(arr)] for i in range(len(arr))]


arr = [12, 10, 5, 6, 52, 36]
n = 2

result = split_and_add(arr, n)

print(*result)


from collections import deque

def splitArr(a, n, k):
q = deque(a)
q.rotate(-k)
return list(q)

# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
print(arr[i], end=' ')
#This code is contributed by Jyothi pinjala.
