# This script calculates your new salary for the next year based on your current salary.
# If your current salary is less than $40,000, you'll get a 5% raise.
# If it's $40,000 or more, you'll get a $2,000 raise plus an additional 2%.
# Enter your first name, last name, and current salary when prompted, and your new salary will be displayed.

def getInfo():
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    salary = float(input("Enter your current salary: "))
    return fName, lName, salary

def calculate(currSal):
    if currSal < 40000:
        newSal = currSal + .05 * currSal
    else:
        newSal = currSal + (2000 + .02 * currSal)
    return newSal

def display(fName, lName, newSalary):
    print("The next year's salary for ", fName, lName, "is", newSalary)

#program starts
fn, ln, sal = getInfo()
newSal = calculate(sal)
display(fn, ln, newSal)
