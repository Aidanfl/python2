# This script searches a text file for lines that start with a specified first name.
# Enter the name of the text file and the first name you're looking for.
# The script will print each line from the file that starts with the given name.

fname = input("Enter a text file name: ")
name = input("Enter a first name: ")
fhandle = open(fname) # Opens the text file that was input
for line in fhandle:
    if line.startswith(name): # If the line starts with the input first name
        print(line) # then the whole line is printed
