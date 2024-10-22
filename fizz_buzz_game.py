# This script defines a function `fizz_buzz()` that returns:
# - "Fizz" if the number is divisible by 3.
# - "Buzz" if the number is divisible by 5.
# - "FizzBuzz" if the number is divisible by both 3 and 5.
# - The number itself if it is divisible by neither 3 nor 5.
# The function is tested with the numbers 3, 5, 15, and 11.

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        res = "FizzBuzz"
    elif number % 3 == 0:
        res = "Fizz"
    elif number % 5 == 0:
        res = "Buzz"
    else:
        res = number
    return res

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(11))
