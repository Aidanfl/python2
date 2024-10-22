# This script prompts the user to enter two numbers.
# It then calculates the sum and the difference of the two numbers.
# The total (sum) and the difference (first number minus second number) are printed.

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

result = float(number1) + float(number2)
diff = float(number1) - float(number2)

print("The total of the two numbers is: ", result)
print("first number minus second number equals: ", diff)
