# This script determines the graduation honors based on the user's GPA.
# If the GPA is 3.9 or higher, the user graduates with "Summa cum laude".
# If the GPA is between 3.6 and 3.89, they graduate with "Magna cum laude".
# If the GPA is between 3.3 and 3.59, they graduate with "Cum laude".
# If the GPA is below 3.3, they graduate without honors.

# input GPA and figure out whether you graduated or honors

gpa = float(input("Enter your GPA: "))

if gpa >= 3.9:
    print("You graduated! Summa cum laude")

elif gpa >= 3.6:
    print("You graduated! Magna cum laude")

elif gpa >= 3.3:
    print("You graduated! Cum laude")

if gpa < 3.3:
    print("You graduated!")
