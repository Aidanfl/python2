# This script reads a list of numbers from a file named "Numbers.txt" and calculates:
# - The smallest number
# - The sum of all the numbers
# - The average of the numbers
# The numbers in the file should be on separate lines, and the script will output these calculated values.

handle = open("Numbers.txt")
small, total, count = 0, 0, 0
for line in handle:
    num = float(line.strip())
    if count == 0:
        small = num
    total += num
    count += 1
    if num < small:
        small = num

average = total / count

handle.close()

print("Smallest number: ", small)
print("Sum of the numbers: ", total)
print("Average of the numbers: ", average)
