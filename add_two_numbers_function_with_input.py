# This script defines a function `addNumbers()` that takes two numbers as input, adds them, and returns the sum.
# The user is prompted to input two numbers, which are passed to the function.
# The sum is then printed.

def addNumbers(num1, num2):
    result = num1 + num2  # add the numbers
    return result  # return the sum

# program starts here
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The sum is:", addNumbers(num1, num2))
