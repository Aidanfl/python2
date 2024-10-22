# This script displays the numbers that are greater than 25 and less than 88.
# It loops through numbers from 3 to 100 and prints only the numbers that fall within the specified range (greater than 25 and less than 88).

# display the numbers that are greater than 25 and less than 88

for num in range(3, 101):
    if num > 25 and num < 88:
        print(num)
