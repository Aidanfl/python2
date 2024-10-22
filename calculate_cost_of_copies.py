# This script calculates the cost of making copies based on the number of copies entered by the user.
# If the number of copies is less than 100, the cost is $0.05 per copy.
# If the number of copies exceeds 100, the first 100 copies cost $0.05 each, and additional copies cost $0.03 each.
# The total cost is then printed.

copies = int(input("Enter number of copies: "))

if copies < 100:
    cost = .05 * copies
    print("The cost is: ", cost, "dollars")

if copies > 100:
    costm = .05 * 100 + ((copies - 100) * .03)
    print("The cost is: ", costm, "dollars")
    
