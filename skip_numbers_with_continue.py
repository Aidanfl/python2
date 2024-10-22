# This script increments the variable `n` from 0 to 9.
# It skips printing the numbers 4 and 6 by using the 'continue' statement.
# The 'continue' statement causes Python to skip the remaining code in the loop for those values and go back to the top of the loop.
# All other numbers are printed.

n = 0
while n <=9:
    n = n + 1
    if n == 4:
        continue # python skips the remaining statements in the while block
                 # and goes back to the beginning of the while loop
    if n == 6:
        continue

    print(n)
