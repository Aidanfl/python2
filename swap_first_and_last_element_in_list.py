# This script swaps the first and last elements of a given list.
# It accesses the first and last elements using indexing, stores them in variables, and then swaps them.
# After the swap, the modified list is printed.

# Given a list, write a Python program to swap first and last element of the list.
aList = [1, 2, 3]

first = aList[0]
last = aList[-1]
aList[0] = last
aList[-1] = first
print(aList)
