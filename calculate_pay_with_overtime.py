# This script calculates the total pay based on hours worked and the hourly rate.
# If the hours worked are greater than 40, the script calculates overtime pay:
# - Regular pay for the first 40 hours: 40 * rate
# - Overtime pay for the additional hours: (hours - 40) * (rate * 1.5)
# If the hours worked are 40 or less, it calculates the pay using the standard rate.
# The total pay is then printed.

#get hours and rate
hours = input("Enter hours: ")
rate = input("Enter rate: ")

hours = float(hours)
rate = float(rate)

#calculate the pay

##if the hours are greater than 40, calculate the pay
##using = 40 * rate + (hours-40)*(rate*1.5)
if hours > 40:
    pay = 40 * rate + (hours - 40) * (rate * 1.5)


##otherwise, calculate the pay using pay = hours * rate
else:
    pay = hours * rate

#display the pay
print("Pay is ", pay)
