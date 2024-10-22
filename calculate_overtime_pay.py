# This script calculates your weekly pay based on the hours worked and hourly rate.
# If you worked 40 hours or less, it multiplies hours by the rate.
# For overtime (hours over 40), it applies a 1.5x rate for the extra hours.
# Enter your hours worked and rate when prompted, and the total pay will be displayed.

def getInfo():
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    return hours, rate

def calculate(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * (1.5 * rate)
    return pay

def display(pay):
    print("Pay is", pay)

def main():
    hours, rate = getInfo()
    pay = calculate(hours, rate)
    display(pay)

main()
