# This script calculates the average, maximum, and minimum of a list of numbers entered by the user.
# The user is repeatedly prompted to enter numbers, and they can stop by typing "done".
# The numbers are stored in a list, and after the user finishes, the script prints the list, the maximum number, the minimum number, and the average.

# Calculate the average of all numbers
lst = list() # lst = []

while True:
    item = input("Enter a number: ")
    if item == "done":
        break
    item = float(item)
    lst.append(item) # add the item from the end user to the list

print(lst)
print("Maximum: ", max(lst))
print("Minimum: ", min(lst))
print("Average: ", sum(lst)/len(lst))
