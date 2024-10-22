# This script defines a function `isEven()` that checks whether a given number is even.
# It prints "Even" if the number is divisible by 2, otherwise it prints "Not even".
# The function is tested with the numbers 6, 9, and 9.8.

def isEven(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Not even")

isEven(6)
isEven(9)
isEven(9.8)
