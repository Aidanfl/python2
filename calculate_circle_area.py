# This script defines a function `radius()` that calculates the area of a circle based on the given radius.
# The formula used is Area = π * r^2, with π approximated as 3.14.
# The user is prompted to enter the radius, and the area of the circle is printed.

#radius of a circle
#function definition
def radius(r):
    return 3.14*(r**2)

r = float(input("Enter the radius: "))
print ("The area of your circle is: ", radius(r))
