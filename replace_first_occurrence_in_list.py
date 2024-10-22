# This script replaces the first occurrence of the number 20 in the list with 200.
# It uses a for loop to iterate through the list, finds the first occurrence of 20,
# replaces it with 200, and then breaks out of the loop.
# The modified list is printed after the replacement.

list1 = [5, 10, 15, 20, 25, 50, 20]

# Method 1 using loop
for index in range(len(list1)):
    if list1[index] == 20:
        list1[index] = 200
        break
print(list1)
