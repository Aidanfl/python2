# This script calculates the sum of all numbers in a list that are greater than 20.
# It iterates through the list of numbers, adds the values greater than 20 to the total sum, and then prints the result.

numbers = [ -9, 8.79, 23, 38.6, 10, -32, 45]
total = 0
for num in numbers:
    if num > 20:
        total += num

print ("The sum is: ", total)


numbers = [-9, 8.79, 23, 38.6, 10, -32, 45]
total = 0
for num in numbers:
    if num > 20:
        total += num

print("The sum is: ", total)
