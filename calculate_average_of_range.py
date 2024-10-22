# This script calculates the average of all numbers in the range from -10 to 100.
# It sums all the numbers in this range, counts how many numbers there are, and then calculates the average.
# The result is rounded to two decimal places and printed.

# average of -10 to 100
total = 0
count = 0

for num in range(-10, 101):
   total = total + num
   count = count + 1

average = total / count

print("The average is: ", round(average, 2))
