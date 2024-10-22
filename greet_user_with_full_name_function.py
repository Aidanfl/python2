# This script defines a function `getFullName()` that prompts the user to enter their full name
# and then prints a greeting with "Good morning" followed by the entered name.
# The function is called twice, allowing the user to enter their full name two times.

# define a function
def getFullName():
    name = input("Enter your full name: ")
    print("Good morning,", name)

# call/use the function
getFullName()
getFullName()
