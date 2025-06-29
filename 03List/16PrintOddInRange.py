# Iterate through all numbers in the given range
for num in range(1, 11):
  
    # check if a number is odd
    if num % 2 != 0:
        print(num)

start = 1
end = 10

# Use list comprehension to create a list of odd numbers
# Iterate through the range (start to end + 1)
odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
print(odd_numbers)