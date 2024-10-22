# This script demonstrates various string operations and functions using the following examples:
# 1. Accessing a character at a specific index in a string ("python"[4]).
# 2. Slicing a string from index 2 to index 2 ("python"[2:2]).
# 3. Slicing a string from the beginning up to index 2 ("python"[:2]).
# 4. Slicing a string starting from index 2 to the end ("python"[2:]).
# 5. Finding the substring "tho" in the string "python" using the find() method.
# 6. Finding the last occurrence of "pp" in the string "whippersnapper" using the rfind() method.
# 7. Finding the first occurrence of "pp" in the string "whippersnapper" using the find() method.
# 8. Counting the occurrences of "k" in the string "Knickknack".
# 9. Using rstrip() to remove trailing spaces from "Gravity   " and getting the length of the result using len().

#Question 1 Part 1
a = "python"[4]
print("1 = ", a)

#Question 1 Part 2
b = "python"[2:2]
print("2 = ", b)

#Question 1 Part 3
c = "python"[:2]
print("3 = ", c)

#Question 1 Part 4
d = "python"[2:]
print("4 = ", d)

#Question 1 Part 5
e = "python".find("tho")
print("5 = ", e)

#Question 1 Part 6
f = "whippersnapper".rfind("pp")
print("6 = ", f)

#Question 1 Part 7
g = "whippersnapper".find("pp")
print("7 = ", g)

#Question 1 Part 8
h = "Knickknack".count("k")
print("8 = ", h)

#Question 1 Part 9
i = len("Gravity   ".rstrip())
print("9 = ", i)
