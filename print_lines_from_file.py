# This script reads through a file named "Numbers.txt" and prints each line as it is read.
# It loops through the file line by line and displays the content of each line.

handle = open("Numbers.txt")
for line in handle: # loop through the file line by line
    print(line)
