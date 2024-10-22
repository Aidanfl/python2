# This script compares two salary options over 10 days:
# 1. Option 1: Earn $100 per day for 10 days.
# 2. Option 2: Earn exponentially increasing amounts starting at $1 on day 1, doubling each day (2^x for day x).
# The script calculates the total earnings for both options and prints the results.
# It then compares the two salaries and prints which option is better.

def option1():
    return 100 * 10 # $100 per day for 10 days

def option2():
    total = 0
    for x in range(10): #range is 10 for 10 days of work
        total += 2 ** x
    return total

salary1 = option1()
salary2 = option2()
print("Outcome:")
print("Option 1 pays $", salary1)
print("Option 2 pays $", salary2)

if salary2 > salary1:
    print("Option 2 is better.")
else:
    print("Option 1 is better.")
