# This script reads a list of U.S. presidents from a file named "USPres.txt" and displays the presidents
# whose numbers fall within a specified range.
# Enter the lower and upper bounds for the range, and the script will print the president numbers and names within that range.
# The file should contain one president's name per line.

with open('USPres.txt', 'r') as handle:
    contents = handle.read()

lowerR = int(input("Enter the lower number for the range: "))
upperR = int(input("Enter the upper number for the range: "))

presnum = 1
while contents:
    newline = contents.find("\n") # ("\n") is used to find the index of the newline character
    presname = contents[:newline].strip()
    contents = contents[newline+1:]
    if lowerR <= presnum <= upperR:
        print(presnum, presname)
    presnum += 1
