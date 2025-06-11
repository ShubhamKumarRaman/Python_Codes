a = [10, 24, 76, 23, 12]

# Max() will return the largest in 'a'
largest = max(a)
print(largest)

a = [10, 24, 76, 23, 12]

# Assuming first element is largest.
largest = a[0]

# Iterate through list and find largest
for val in a:
    if val > largest:
      
      	# If current element is greater than largest
    	# update it
        largest = val

print(largest)

from functools import reduce

a = [10, 24, 76, 23, 12]

# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, a)

print(largest)