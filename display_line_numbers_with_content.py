# This script reads through a file and displays each line along with its line number.
# It loops through the file, increments a counter for each line, and prints the line number followed by the content of the line.

# display the line number with line content
handle = open("example.txt")
count = 0
for line in handle: # loop through the file line by line
    count = count + 1
    print(count, line)
