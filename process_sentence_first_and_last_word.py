# This script processes a user-input sentence by removing punctuation (periods, exclamation marks, question marks),
# then splits the sentence into words. It extracts the first and last words and calculates their lengths.
# Finally, it prints the first and last words along with their respective lengths.

# Input
sentence = input("Enter a sentence: ")

# Remove punctuation
sentence = sentence.rstrip(".!?")

# Split sentence
words = sentence.split()

# Get first and last words + lengths
firstw = words[0]
lastw = words[-1]
firstwLen = len(firstw)
lastwLen = len(lastw)

# Print
print("First word is", firstw, "the length is", firstwLen)
print("Last word is", lastw, "the length is", lastwLen)
