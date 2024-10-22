# This script calculates the user's pay based on the number of hours worked and the hourly rate.
# It prompts the user to input the hours worked and the rate per hour.
# The inputs are converted to float values and the total pay is calculated by multiplying hours by the rate.
# The calculated pay is then printed.

hours = input("Enter hours: ")
rate = input("Enter rate: ")

hours = float(hours)
rate = float(rate)

pay = hours * rate

print("Your pay is: ", pay)
