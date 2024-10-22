# This script generates a dictionary where the keys are numbers from 1 to a user-defined value 'n',
# and the values are the squares of the keys.
# The user is prompted to enter a number 'n', and the script creates a dictionary with key-value pairs (x: x*x) from 1 to n.
# The dictionary is then printed as the expected output.

n = int(input("Enter a number: "))

dictionary = {}

for x in range(1, n+1):
    dictionary[x] = x*x

print("Sample Dictionary =", n)
print("Expected Output: ", dictionary)
