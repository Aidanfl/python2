# This script counts the occurrences of the letter "a" in the string "banana".
# It loops through each character in the string, checks if it is "a", and increments a counter.
# The total count of "a" occurrences is printed at the end.

s = "banana"
# count the occurrence of "a"
count = 0
for ch in s:
    if ch == "a":
        count = count + 1

print("a appears", count, "times")
