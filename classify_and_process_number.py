# This script prompts the user to input a number and performs the following checks and operations:
# - If the number is positive, it prints "positive number", subtracts 100 from it, and prints the result.
#   If the number is greater than 100, it also prints "big".
# - If the number is negative, it prints "negative number", adds 100 to it, and prints the result.
#   If the number is less than -100, it also prints "small".
# - If the number is 0, it prints "equals zero".
# After all checks, it prints "Done".

num = input("Enter a number: ")

num = float(num)

if num > 0:
    print("positive number")
    result = num - 100
    print(num, "-", 100, "=", result)
    if num > 100:
        print("big")
        

if num < 0:
    print("negative number")
    result = num + 100
    print(num, "+", 100, "=", result)
    if num < -100:
        print("small")

if num == 0:
    print("equals zero")

print("Done")
