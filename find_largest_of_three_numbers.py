# This script defines a function `max_num()` that takes three numbers and returns the largest of them.
# The function compares the three numbers and returns the largest.
# The user is prompted to input three numbers, and the largest is printed.

#function definition
def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

#program starts
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("Enter a number: "))
print("The largest number is: ", max_num(a, b, c))
