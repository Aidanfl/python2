# This script squares each element in a given list.
# It loops through the list, squares each element, and updates the list with the squared values.
# After squaring all the elements, the modified list is printed.

aList = [1, 2, 3, 4, 5, 6, 7]

for index in range(len(aList)):
    num = aList[index]
    aList[index] = num * num

print(aList)
