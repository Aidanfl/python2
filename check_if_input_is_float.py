# This script defines a function `isfloat()` that checks if a given input can be converted to a float.
# The user is prompted to enter a number, and the script verifies whether the input is a valid float.
# It prints a message indicating whether the input is a valid float or not.

def isfloat(value):
    try:
        float(value)  # Try converting the value to a float
        return True    # If successful, return True
    except ValueError:
        return False   # If a ValueError occurs, return False

# Get user input
user_input = input("Enter a number: ")

# Check if the input is a float
if isfloat(user_input):
    print(f"{user_input} is a valid float.")
else:
    print(f"{user_input} is not a valid float.")
