# This script opens a file named "Numbers.txt" and reads its entire content into a string.
# It then prints the content of the file.

handle = open("Numbers.txt")
s = handle.read() # read the whole content of the file to a string as a string

print(s)
