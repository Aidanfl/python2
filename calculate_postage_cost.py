# Enter the weight of your letter in ounces, and this script will calculate the postage cost.
# The first ounce costs 5 cents, and each additional ounce costs 10 cents.
# The cost will be converted to dollars and displayed in a formatted string.

import math

def cost(weight):
    # Compute the postage cost based on the weight
    base_cost = 5   # 5 cents for the first ounce
    additional_cost = 10  # 10 cents for each additional ounce
    total_cost = base_cost + additional_cost * math.ceil(weight - 1)
    
    # Convert the cost to dollars and format the output
    cost_in_dollars = total_cost / 100
    formatted_cost = "${:.2f}".format(cost_in_dollars)
    
    # Return the formatted cost as a string
    return formatted_cost

# Get the weight of the letter from the user
weight = float(input("Enter the number of ounces: "))

# Calculate the cost of postage and print the result
postage_cost = cost(weight)
print("Cost: " + postage_cost)
