# This code finds the remainder of the product of all the elements in the array arr divided by 'n'.
def findremainder(arr, len, n):
	product = 1
	for i in range(len):
		product = product * arr[i]
	return product % n


arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findremainder(arr, len, n))


# Python3 program to
# find remainder when
# all array elements
# are multiplied.

# Find remainder of arr[0] * arr[1]
# * .. * arr[n-1]
def findremainder(arr, lens, n):
	mul = 1

	# find the individual
	# remainder and 
	# multiple with mul.
	for i in range(lens): 
		mul = (mul * (arr[i] % n)) % n
	
	return mul % n

# Driven code
arr = [ 100, 10, 5, 25, 35, 14 ]
lens = len(arr)
n = 11

# print the remainder
# of after multiple
# all the numbers
print( findremainder(arr, lens, n))

from functools import reduce

def remainderAfterMultiplication(arr, n):
	result = reduce(lambda x, y: (x * y) % n, arr)
	return result

# Driver Code
arr1 = [100, 10, 5, 25, 35, 14]
n1 = 11
result1 = remainderAfterMultiplication(arr1, n1)
print(result1)

arr2 = [100, 10]
n2 = 5
result2 = remainderAfterMultiplication(arr2, n2)
print(result2)
