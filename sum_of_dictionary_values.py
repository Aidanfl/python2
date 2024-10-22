# This script calculates the sum of all values in a dictionary.
# It iterates through the dictionary, retrieves each value, and adds it to a list.
# The sum() function is then used to calculate the total of the values, and the result is printed.

#Given a dictionary in Python,
# write a Python program to find the sum of all Items in the dictionary. 
d = {'x': 25, 'y':18, 'z':45}

lst = []
for key in d:
    value = d[key]
    lst.append(value)
total = sum(lst)
print("Total: ", total)
