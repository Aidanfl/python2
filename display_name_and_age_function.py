# This script defines a function `display()` that takes a name and an age as arguments and prints them.
# The function is tested twice:
# 1. With hardcoded values ("Aidan" and 21).
# 2. With user inputs for the name and age.

#Question 1
def display(name, age):
    print("Your name is ", name)
    print("Your age is ", age)

#use constants test the function
display("Aidan", 21)

#use user inputs to test the function
name = input("Enter your name: ")
age = input("Enter your age: ")
display(name, age)
