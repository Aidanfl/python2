# This script removes all occurrences of the number 20 from a list.
# It first counts how many times 20 appears in the list using the count() method.
# Then, it uses a for loop to remove 20 that many times with the remove() method.
# The modified list is printed after all occurrences of 20 are removed.

list1 = [5, 10, 15, 20, 25, 50, 20]

# Get the number of 20s using count(), then use remove() for so many times
c = list1.count(20)

for i in range(c):
    list1.remove(20)

print(list1)
