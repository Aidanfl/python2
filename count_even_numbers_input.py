# This script counts the number of even numbers entered by the user.
# The user is prompted to enter numbers repeatedly until they type "Done".
# For each entered number, if it is even, the count is incremented.
# After the user finishes inputting numbers, the total count of even numbers is printed.

count = 0
while True:
    number = input("Enter a number (or 'Done' to finish): ")
    if number.lower() == "done":
        break
    try:
        if int(number) % 2 == 0:
            count += 1
    except ValueError:
        print("Please enter a valid integer or 'Done' to exit.")

print("There are", count, "even numbers.")
