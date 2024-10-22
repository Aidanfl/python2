# This script defines a function `addTwoNumbers()` that takes two numbers as arguments,
# adds them, and returns the total.
# The user is prompted to input two numbers, which are passed to the function.
# The returned result is then printed as the total.

def addTwoNumbers(number1, number2):
    total = number1 + number2
    return total


# program starts here
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

result = addTwoNumbers(num1, num2)  # store the returned value to result

print("Total is", result)
