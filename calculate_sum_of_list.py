# This script calculates the total (sum) of all numbers in a given list.
# It iterates through the list, adding each number to a total variable.
# After the loop, the total sum of the list is printed.

total = 0

for num in [-100, 9, 41, 12, 3, 74, 15, 30, 345, 2]:
   total = total + num

print("The total of the list is: ", total)
