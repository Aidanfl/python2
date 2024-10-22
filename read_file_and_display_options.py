# This script opens a file named "Numbers.txt" and reads its entire content into a string.
# It prints the content of the file, then calculates and displays the number of characters in the string.
# After that, it presents a simple menu with options to add, subtract, or multiply (though no operations are performed).

handle = open("Numbers.txt")
s = handle.read() # read the whole content of the file to a string as a string
print(s) # "6\n9\n2\n3\n6\n4"

print("The number of characters in s is", len(s))
print("1. add\n2. subtract\n3. multiplication")
