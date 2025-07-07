start = -5
end = 3

# Loop through range and print positive numbers
for val in range(start, end + 1):
  
    # checks whether current number is positive
    if val > 0:
        print(val)

start = -5
end = 3

# Use list comprehension to filter positive numbers and print them
res = [val for val in range(start, end + 1) if val > 0]
print(res)

start = -5
end = 3

# Use filter to get positive numbers
res = filter(lambda val: val > 0, range(start, end + 1))

# Convert filter object to list and print
print(list(res))