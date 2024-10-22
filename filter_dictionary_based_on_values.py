# This script filters a dictionary based on the values.
# It takes a dictionary of names and heights, and filters out the entries where the height is greater than 170.
# The filtered items are added to a new dictionary, which is then printed.

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d1 = {}

for key, value in d.items():
    if value> 170:
        d1[key] = value # Add the item to a new dictionary

print("New dictionary with marks greater than 170\n", d1)
