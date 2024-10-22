# This script prompts the user to enter two numbers, converts them to floats, and performs basic arithmetic operations:
# - Addition
# - Subtraction
# - Multiplication
# The results are then printed.

"""
Author: Alice
Date: 1/24/2023
Function: a simple calculator
"""

#get inputs from end users

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

#convert the two inputs into numbers
number1 = float(number1)
number2 = float(number2)

#do calculation
result = number1 + number2
diff = number1 - number2
mul = number1 * number2

#display the results
print("The total of the two numbers is: ", result)
print("first number minus second number equals: ", diff)
