# This script allows the user to input 8 letters, then calculates and displays the following:
# 1. The largest letter (alphabetically).
# 2. The smallest letter (alphabetically).
# 3. The number of occurrences of each letter, sorted by frequency in descending order.
# It uses the Counter class from the collections module to count occurrences and sorts them based on the count.

from collections import Counter

letters = []

# Input
for i in range(8):
    letter = input("Enter a letter: ")
    letters.append(letter)

# Calculate largest and smallest
LargestL = max(letters)
smallestL = min(letters)

# Count occurrences
CounterL = Counter(letters)

# Sort letters Desc
occurrences = sorted(CounterL.items(), reverse=True)

def SortO(LetterTuple):
    return LetterTuple[1]

sortedLetters = sorted(occurrences, key=SortO, reverse=True)

# Print
print("The largest letter is:", LargestL)
print("The smallest letter is:", smallestL)
print("Letter occurrences:")

for letter, count in sortedLetters:
    print(letter, ":", count)
