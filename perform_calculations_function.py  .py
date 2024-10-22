# This script defines a function `calculation()` that performs three operations (addition, subtraction, and multiplication)
# on two numbers and returns the results.
# The function is tested in two ways:
# 1. Using hardcoded values (9 and 6).
# 2. Using numbers entered by the user.
# The results are then printed (sum, subtraction, and multiplication).

#function definition

def calculation(num1, num2):
    total = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    return total, sub, mul

#program starts
print(calculation (9, 6)) #method1_testing using constants
#method2_using inputs from end users
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
t, s, m = calculation(number1, number2)
print("The sum is", t)
print("The subtraction is", s)
print("The multiplication is", m)
