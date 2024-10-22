# This script demonstrates three different methods for multiplying all the values in a dictionary.
# The dictionary contains key-value pairs, and the script calculates the product of all the values in three different ways:
# 1. Using the dictionary items.
# 2. Using the values() method to extract the values as a list and multiply them.
# 3. Using the dictionary keys to access the values and multiply them.

d = {'data1': 100,'data2': -54,'data3': 247}

# Method 1
mul = 1
for key, value in d.items():
    mul = mul * value

# Method 2
lst = d.values()
for v in lst:
    mul = mul * v

# Method 3
mul = 1
for key in d:
    mul = mul * d[key]
