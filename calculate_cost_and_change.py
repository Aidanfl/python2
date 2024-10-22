# This script calculates the total cost based on the weight of an item in pounds and a fixed price per pound ($2.50).
# The user is prompted to enter the weight and the amount of payment in dollars.
# The script calculates whether the user has paid enough, and if so, it provides the change.
# If the change is less than $1, it prints an additional message.
# If the payment is insufficient, it calculates how much more the user owes.

weight = float(input("Enter weight in pounds: "))
payment = float(input("Enter payment in dollars: "))

price = 2.5
cost = price * weight

if payment >= cost:
    change = payment - cost
    print("Your change is $" + str(round(change, 2)) + ".")
    if change < 1:
        print("Change is less than $1.")

else:
    diff = cost - payment
    print("You owe $" + str(round(diff, 2)) + " more.")
