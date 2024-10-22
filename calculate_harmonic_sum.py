# This script calculates the harmonic sum of the numbers from 1 to 100.
# It adds the reciprocal of each number from 1 to 100 to a running total.
# The result is rounded to two decimal places and printed.

total = 0
for num in range(1, 101):
    total = total + 1/num

print("The total is", round(total, 2))
