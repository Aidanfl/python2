# This script opens a file named "Numbers.txt" and reads the first two characters from the file.
# It prints those two characters to the console.
# Note: The number of characters to be read is specified as 2 in the read() function.

handle = open("Numbers.txt")
s = handle.read(2) # read the whole content of the file to a string as a string
print(s) # "6\n9\n2\n3\n6\n4"
