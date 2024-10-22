# This script defines a function `GetNumbers()` that:
# 1. Prompts the user to enter two numbers.
# 2. Adds the two numbers.
# 3. Displays the result in the form "num1 + num2 = total".
# The function is called to perform the above tasks.

def GetNumbers():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    total = num1 + num2
    print(num1, "+", num2, "=", total)


# call/use the function
GetNumbers()
