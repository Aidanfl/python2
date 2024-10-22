# This script allows the user up to 3 attempts to enter the correct PIN.
# The correct PIN is "12345". After each incorrect attempt, the user is prompted to try again.
# If the user enters the correct PIN, the script prints "Correct, welcome back." and exits.
# If the maximum number of tries (3) is reached without a correct entry, the script prints "Sorry but you have been locked out."

# Create a code with a maximum of 3 tries
MAX_TRIES = 3
PIN = "12345"

tries = 0
while tries < MAX_TRIES:
    pin_input = input("Please enter the PIN: ")
    tries += 1
    
    if pin_input == PIN:
        print("Correct, welcome back.")
        break
    else:
        print("Incorrect, try again.")
        
if tries == MAX_TRIES:
    print("Sorry but you have been locked out.")

