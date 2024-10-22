# This script prompts the user to enter a number and displays a message based on the number's value:
# - If the number is less than 0, it prints "Negative".
# - If the number is between 0 and 10 (inclusive), it prints "Small".
# - If the number is between 10 and 20 (inclusive), it prints "Medium".
# - If the number is greater than 20, it prints "Large".

# number < 0: negative
# 0 <= number < 10: small
# 10 <= number < 20: medium
# number> 20: large

num = float(input("Enter a number: "))

if num < 0:
    print("Negative")

if 0 <= num < 10:
    print("Small")

if 10 <= num < 20:
    print("Medium")

if num > 20:
    print("Large")
