# This script calculates the total cost of bagels based on the number of bagels purchased.
# If fewer than 6 bagels are purchased, each bagel costs $0.90.
# If 6 or more bagels are purchased, each bagel costs $0.40.
# The script prompts the user to enter the number of bagels and then prints the total cost.

num = int(input("Enter number of bagels: "))

if num < 6:
    cost = 0.9 * num
    print("Cost is: ", cost)

if num >= 6:
    cost = 0.4 * num
    print("Cost is: ", cost)