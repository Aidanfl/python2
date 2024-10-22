# This script extracts and prints the middle name from a full name input by the user.
# The user is prompted to enter their first, middle, and last name.
# The script splits the input into individual words using the split() method.
# If exactly three names are entered, it prints the middle name. If there are too many or too few names, it prints an error message.

name = input(str("Input your first, middle and last name: "))

each = name.split()

if len(each) == 3:
    print("Your middle name is: ", each[1])
else:
    print("You have too many names :(")
