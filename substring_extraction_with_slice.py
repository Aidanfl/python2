# This script demonstrates how to use the slicing operator to extract a substring from a string.
# It extracts characters from index 0 to index 2 (inclusive of 0, but excluding 3) from the string "banana".
# The substring is then printed.

s = "banana"
# : operator s[num1 : num2] or "banana"[num1 : num2]
# num1 is the starting index value of the substring
# num2 is the greater than the ending index value
# (up to num 2 or num 2 is not included)
# print(s[0]+s[1]+s[2])

print(s[0:3])
