# This script defines a function `display()` that prints the message "Spring is here!" multiple times.
# The user is prompted to enter a positive number, and the script prints the message that many times.

def display(n):
    for i in range(n):
        print("Spring is here!")

number = int(input("Enter a positive number: "))
display(number)
