a = [10, 20, 4, 45, 99]

# Initialize largest (max1)
# and second largest (max2) to negative infinity
max1 = max2 = float('-inf')

# Loop through each number in list
for n in a:
  
    # If the current number is greater 
    # than largest found so far
    if n > max1:
      
        # Update second largest to the previous largest
        max2 = max1  
        
        # Update largest to the current number
        max1 = n     
        
    # If current number is less than largest
    # but greater than second largest
    elif n > max2 and n != max1:
      
        # Update second largest to current number
        max2 = n  

print(max2)

a = [10, 20, 4, 45, 99]

# Sorting the list in descending order
a.sort(reverse=True)

# Second largest number will be at index 1
print(a[1])

import heapq

a = [10, 20, 4, 45, 99]

# Get the two largest numbers using heapq.nlargest
top_two = heapq.nlargest(2, a)

# The second largest number is at index 1
print(top_two[1])