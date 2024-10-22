# This script reads a file named "Numbers.txt" and displays all the numbers line by line.
# It opens the file, removes any trailing whitespace from each line using rstrip(), and then prints the line.

fhandle = open("Numbers.txt")

for line in fhandle:
    line = line.rstrip()
    print(line)
