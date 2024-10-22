# This script calculates the frequencies of words in a predefined list of words.
# It creates a dictionary where each word is a key, and the value is the number of times the word appears in the list.
# The word frequencies are then printed.

lst = ["the", "clown", "ran", "after", "the", "car", "and"]
d = {}
for item in lst:
    d[item] = d.get(item, 0) + 1 # Is equivalent to the if else block
print(d)
