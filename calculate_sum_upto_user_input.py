# This script calculates the total sum of all integer numbers from 1 to a number entered by the user.
# The user is prompted to input a number, and the script sums all integers from 1 up to and including the user's number.
# The total sum is then printed.

# get a number from end users, then calculate all integer numbers
# between 1 and this number
total = 0
x = int(input("Enter a number: "))

for num in range(1, x + 1):
   total = total + num

print("The total of the list is: ", total)
