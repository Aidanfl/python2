# This script filters a dictionary by removing key-value pairs where the value is None.
# It iterates through the original dictionary and adds only the key-value pairs where the value is not None to a new dictionary.
# After filtering, the new dictionary is printed.

d = {'c1': 'Red', 'c2': 'Green', 'c3': None}
d1 = {}

for key, value in d.items():
    if value is not None:
        d1[key] = value # Add the item to a new dictionary
print("New dictionary after dropping the empty item\n", d1)
