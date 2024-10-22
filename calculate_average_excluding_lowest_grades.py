# This script takes 5 grades as input, sorts them, and removes the lowest two grades.
# After removing the lowest grades, it calculates the average of the remaining three grades.
# The sorted list and the average are then displayed.

## Input of 5 grades into dictionary
grades = []
for f in range(5):
    grade = float(input("Enter grade #" + str(f+1) + ": ")) # str(f+1) creates a loop to enter in 5 seperate grades
    grades.append(grade)

## Sort grades small to large and remove lowest two grades
grades.sort() # Sorts the grades
grades = grades[2:]
print(grades)

## Calculation of average
average = sum(grades) / len(grades)


print("Average without lowest two scores:", average)
