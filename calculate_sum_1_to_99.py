# This script calculates the total (sum) of all numbers from 1 to 99.
# It iterates through the range from 1 to 99 and adds each number to a total variable.
# After the loop, the total sum is printed.
# Note: The range(1, 100) excludes 100, so the total will be for numbers 1 through 99.

# total of 1 to 100
total = 0

for num in range(1, 100):
   total = total + num

print("The total of the list is: ", total)
