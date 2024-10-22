# This script calculates the total amount of money a user will earn before retiring at the age of 65.
# It prompts the user to input their name, age, and current salary.
# The script then assumes a 5% salary increase each year and calculates the total earnings from the user's current age until 65.
# The final total is printed with the user's name and rounded to two decimal places.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your current salary: "))

total = 0
for i in range(age, 65):
    total = total + salary
    salary = salary + salary * 5/100

print(name, "will earn$" + str(round(total, 2)), "before retiring")