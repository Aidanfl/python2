# This script prompts the user to enter two numbers.
# It converts the input into float values and then performs three operations:
# 1. Calculates the sum of the two numbers.
# 2. Calculates the difference (first number minus second number).
# 3. Calculates the multiplication of the two numbers.
# The results of these operations are then printed.

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

number1 = float(number1)
number2 = float(number2)

result = number1 + number2
diff = number1 - number2
mul = number1 * number2

print("The total of the two numbers is: ", result)
print("first number minus second number equals: ", diff)
