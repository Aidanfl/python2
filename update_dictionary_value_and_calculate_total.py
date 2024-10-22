# This script updates the value associated with the key "Aaron" in the dictionary 'homeRunKings' to 800.
# It then calculates the total number of home runs hit by summing the values in the dictionary.
# The updated dictionary and the total number of home runs are printed.

# Update the value of "Aaron" with 800
homeRunKings = {"Bonds": 762, "Aaron": 755}
homeRunKings["Aaron"] = 800

# Calculate the total number of home runs hit in homeRunKings
totalHR = sum(homeRunKings.values())

# Print each answer
print("Updated homeRunKings:", homeRunKings)
print("Total home runs:", totalHR)
