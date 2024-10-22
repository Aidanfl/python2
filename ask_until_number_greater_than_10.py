# This script continuously asks the user to enter a number until the number is greater than 10.
# If the entered number is greater than 10, it prints "Done" and exits the loop.
# Otherwise, it asks the user to try again.

# keep asking end users to enter a number, if the number is greater than 10,
# print "Done", else ask the user to try again.

while True:
    number = input("Enter a number: ")
    number = float(number)
    if number > 10:
        break # python jumps out of the loop when break is executed
    else:
        print("Try again.")
print("Done")
