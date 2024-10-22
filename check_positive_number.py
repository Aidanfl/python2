# This script prompts the user to enter a number and checks if it is positive.
# It converts the input to a float and prints "positive number" if the number is greater than 0.

try:
    num = input("Enter a number: ")
    num = float(num)

    if num > 0:
        print("Positive number")
    elif num == 0:
        print("The number is zero")
    else:
        print("Negative number")
except ValueError:
    print("Please enter a valid number.")
