# This script demonstrates how to concatenate two lists and then sort the result.
# It creates two lists: 'a' with values [9, 1, 7, 2] and 'b' with values [4, 8, 6].
# The lists are concatenated using the '+' operator and stored in 'm'.
# The resulting list is then sorted in ascending order and printed.

a = [9, 1, 7, 2]
b = [4, 8, 6] 

m = a + b
m.sort()

print(m)
