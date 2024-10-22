# This script calculates whether a company is at a profit, loss, or breakeven based on cost and revenue.
# The user is prompted to input the company's cost and revenue.
# The script then checks:
# - If cost equals revenue, it prints "breakeven".
# - If cost is greater than revenue, it calculates and prints the loss.
# - If cost is less than revenue, it calculates and prints the profit.

# get cost and revenue with possible break even

cost = float(input("Cost of company: "))

revenue = float(input("Revenue of company: "))

if cost == revenue:
    print("breakeven")

if cost > revenue:
    loss = revenue - cost
    print ("loss is: ", loss)

if cost < revenue:
    profit = revenue -  cost
    print ("revenue is: ", cost)

