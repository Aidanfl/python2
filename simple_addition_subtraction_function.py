# This script defines a function `calculation()` that performs addition and subtraction on two numbers.
# The function returns both the sum and the difference of the two numbers.
# The function is called with the values 40 and 10, and the results are printed.

#function definition

def calculation(a, b):
    total = a + b
    sub = a - b
    return total, sub

res = calculation(40, 10)

print(res)
