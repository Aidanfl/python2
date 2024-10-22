# This script opens a file named "Numbers.txt" in write mode and writes the string "Hello" to it.
# It then prints the file handle to the console.
# Note: Writing to the file in this mode will overwrite any existing content in "Numbers.txt".

handle = open("Numbers.txt", "w")
handle.write("Hello")

print(handle)
