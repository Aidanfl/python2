# This script counts the number of words in a sentence provided by the user.
# If the sentence ends with a period, it removes the period before counting.
# The sentence is split into words using the split() method, and the total number of words is printed.

sentence = input("Enter a sentence: ")
wordcount = 0

# Remove the period if the sentence ends with one
if sentence.endswith("."):
    sentence = sentence[:-1]

# Split the sentence into words
words = sentence.split()

# Count the number of words
wordcount = len(words)

print("The sentence contains", wordcount, "words.")
