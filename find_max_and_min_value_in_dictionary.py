# This script finds the maximum and minimum values in a dictionary.
# It extracts the values from the dictionary using the values() method.
# The script then uses the max() and min() functions to find the largest and smallest values, and prints the results.

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
lst = d.values()

biggest = max(lst)
smallest = min(lst)
print("Maximum: ", biggest)
print("Minimum: ", smallest)

