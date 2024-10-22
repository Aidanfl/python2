# This script prompts the user to enter a name three times in a while loop.
# It prints each entered name and continues until the loop runs 3 times (n = 0 to 2).

n = 0
while n <= 2:
    name = input("Enter a name: ")
    print(name)
    n = n + 1
