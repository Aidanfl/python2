# This script continuously asks the user to enter a 4-digit number and a username.
# If the entered number equals "1234" and the username is "BonerKiller44", it prints "Correct" and exits the loop.
# Otherwise, it asks the user to try again.

# keep asking end users to enter a 4-digit number and username,
# if the number equals "1234", and username is "BonerKiller44"
# print "Done", else ask the user to try again.

while True:
    number = input("Enter a 4-digit code: ")
    username = input("Enter your username: ")
    if number == "1234" and username == "BonerKiller44":
        break
    else:
        print("Try again.")
        
print("Correct")
