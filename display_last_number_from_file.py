# This script reads a file named "Numbers.txt" and displays the last number in the file.
# It loops through each line in the file and uses the 'pass' statement to skip all lines except the last one.
# After the loop, the last line (number) is printed.

# Display the last number
fhandle = open("Numbers.txt")

for line in fhandle:
    pass

print(line)
