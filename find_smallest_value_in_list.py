# This script finds the smallest value in a given list of numbers using a for loop.
# It starts with a variable `small` initialized to None.
# As it iterates through the list, it checks if the current number is smaller than the value of `small` and updates `small` accordingly.
# The smallest number in the list is printed at the end.

# Find the smallest value in a list using a for loop
small = None

for num in [9, 41, 12, 3, 74, 15]:
    if small is None:
        small = num
    elif num < small:
        small = num

print("The smallest number is: ", small)
