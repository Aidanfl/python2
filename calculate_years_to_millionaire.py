# This script calculates how many years it will take for an initial deposit to reach $1,000,000 with a 4% annual interest rate.
# The user is prompted to input the initial deposit.
# The script then loops, adding 4% of the current balance each year, and counts the number of years required.
# It prints the balance and the number of years after each iteration.
# Once the balance reaches $1,000,000 or more, the script prints the total number of years taken to become a millionaire.

balance = float(input("Enter your deposit: "))

year = 0

while balance < 1000000:
    balance =  balance + .04 * balance
    year =  year + 1
    print(year, balance)

print("After", year, "years, you will be a millionaire")
