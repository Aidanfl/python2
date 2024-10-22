# This script finds the largest number in a given list of numbers.
# It initializes the largest number as None, then iterates through the list.
# On the first iteration, the first value is assigned to the largest variable.
# For each subsequent iteration, the script compares the current number to the largest value and updates it if necessary.
# After the loop, the largest number is printed.

largest = None # None is keyword, means unknown

for num in [-100, 9, 41, 12, 3, 74, 15, 30, 345, 2]:
    if largest is None: # first iteration, assign the first value to largest
                    # is a keyword, siilar to ==, but stronger
        largest = num
    elif num > largest:
        largest = num # from second interation, compare num with largest
print("The largest number is: ", largest)
