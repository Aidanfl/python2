# This script reads a file named "Numbers.txt" and finds the largest number in the file.
# It loops through each line, converts it to an integer, and keeps track of the largest number encountered.
# After the loop, it prints the largest number.

# Display the largest number
fhandle = open("Numbers.txt")
largest = None

for line in fhandle:
    line = int(line)
    if largest is None:
        largest = line
    elif line > largest:
        largest = line
print(largest)
