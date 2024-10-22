# This script counts the frequency of each letter in the string 'w3resource'.
# It creates a dictionary where the keys are the letters and the values are the counts of how many times each letter appears.
# The script loops through each letter in the string, checks if the letter is already in the dictionary, and updates the count accordingly.
# The updated dictionary is printed after each iteration.

s = 'w3resource'
d = {}
for letter in s:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] = d[letter] + 1

    print(d)
