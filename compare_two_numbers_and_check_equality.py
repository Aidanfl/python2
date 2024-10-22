# This script compares two numbers entered by the user.
# It prints the larger of the two numbers, or prints a message indicating that the numbers are equal if they are the same.

# Display the larger of two numbers and if they are equal

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(num1)

elif num1 < num2:
    print(num2)

else: # num1 == num2
    print("The two numbers are equal. ")