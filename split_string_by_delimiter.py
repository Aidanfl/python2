# This script demonstrates how to split a string into a list using a specified delimiter.
# It takes the string 'words' with the value "first@second@third" and splits it using the '@' character.
# The resulting list 'things' is then printed, which contains the individual segments of the original string.

words = "first@second@third"
things = words.split('@')
print(things)
