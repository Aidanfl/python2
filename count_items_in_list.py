# This script counts the number of items in a given list of numbers.
# It iterates through the list, incrementing a counter for each item.
# After the loop, the total count of items in the list is printed.

count = 0

for num in [-100, 9, 41, 12, 3, 74, 15, 30, 345, 2]:
   count = count + 1

print("The number of items in the list is: ", count)
