# This script prompts the user to input two numbers, then compares them.
# If the first number is larger, it prints the first number and "Number 1 is larger".
# If the second number is larger, it prints the second number and "Number 2 is larger".
# The numbers are first converted to floats before comparison.

num1 = input("Number one: ")
num2 = input("Number two: ")

num1 = float(num1)
num2 = float(num2)

if num1 > num2:
    print (num1)
    print ("Number 1 is larger")

if num2 > num1:
    print(num2)
    print ("Number 2 is larger")
