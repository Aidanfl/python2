# This script counts the number of digits to the left and right of the decimal point in a given number.
# The user is prompted to input a number, and the script finds the position of the decimal point.
# It calculates the number of digits to the left and right of the decimal point and prints the results.

number = input("Enter number: ")
n1 = number.find('.')
n2 = len(number) - (n1 + 1)
print(n1, "digits to left of the decimal point")
print(n2, "digits to right of the decimal point") 
