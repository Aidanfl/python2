# This script prompts the user to enter a number and checks its value against specified ranges.
# - If the number is greater than 20, it prints "Above 20".
# - If the number is greater than 5 but less than or equal to 20, it prints "Above 5".
# - If the number is greater than 10 but less than or equal to 5, it prints "Above 10".
# - For all other values, it prints "Something else".

x = float(input("Enter: "))

if x > 20:
    print('Above 20')
elif x > 10:
    print('Above 10')
elif x > 5:
    print('Above 5')
else:
    print('Something else')
