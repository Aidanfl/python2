# This script increments the variable `n` by 4 starting from -3 until it reaches 25.
# It skips printing numbers that are divisible by 3.
# Additionally, it only prints numbers that are greater than 10 and less than 22.

n = -3

while n <= 25:
    n = n + 4
    if n % 3 == 0:
        continue
    if n > 10 and n < 22:
        print(n)
