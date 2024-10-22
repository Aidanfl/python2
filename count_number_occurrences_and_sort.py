# This script takes 8 numbers as input from the user and counts how many times each number occurs.
# It stores the occurrences in a dictionary where the keys are the numbers and the values are the counts.
# After collecting the input, it sorts the dictionary by the numbers and prints each number with its count.
# A final message is printed thanking the user.

## New empty Dictionary
occurrences = {}

## Loop 8 inputs
for i in range(8):
    num = int(input("Enter a number: "))
    
# If num in dict, increase num by one
    if num in occurrences:
        occurrences[num] += 1
# if num not in dict, add it with a count of 1
    else:
        occurrences[num] = 1

# Sort the dictionary by number
for number, count in sorted(occurrences.items()):
    print(f"{number}: {count}")

print("Thanks for letting me retake this quiz!")
