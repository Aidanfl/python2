# This script uses the 'in' operator to check if a specific character ("$") is present in the string "banana$".
# If the character is found, it prints "Found"; otherwise, it prints "Not found".

s = "banana$"
# in operator is used to check if a character or a substring in a string

if "$" in s:
    print("Found")
else:
    print("Not found")
