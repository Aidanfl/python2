# This script finds the smallest number in a given list of numbers.
# It initializes the smallest number as None, then iterates through the list.
# On the first iteration, the first value is assigned to the smallest variable.
# For each subsequent iteration, the script compares the current number to the smallest value and updates it if necessary.
# After the loop, the smallest number is printed.

smallest = None # None is keyword, means unknown

for num in [-100, 9, 41, 12, 3, 74, 15, 30, 345, 2]:
    if smallest is None: # first iteration, assign the first value to largest
                    # is a keyword, siilar to ==, but stronger
        smallest = num
    elif num < smallest:
        smallest = num # from second interation, compare num with largest
print("The smallest number is: ", smallest)
