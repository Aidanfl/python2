# This script counts the number of even and odd numbers in a range from 1 to 9.
# It loops through the numbers, checks if each number is even or odd, and increments the respective counter.
# After the loop, it prints the total count of even and odd numbers.

countEven = 0
countOdd = 0
for num in range(1, 10):
    if num % 2 == 0:
        countEven = countEven + 1
    else:
        countOdd = countOdd + 1
print("There are", countEven, "even numbers in this list")
print("There are", countOdd, "odd numbers in this list")
