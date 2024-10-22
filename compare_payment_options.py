# This script defines two payment options and compares them to determine which is better.
# Option 1 calculates a total by multiplying 330 by 20.
# Option 2 calculates a total by starting with a payment of 1 and increasing it by 50% each time over 20 iterations.
# The script calls both functions, converts Option 1 to a float, and compares the results.
# It then prints the results and states which option is better.

def option1():
    return 330 * 20

def option2():
    total = 0
    pay = 1
    for i in range(20):
        total = total + pay
        pay = pay + (pay * 50/100)
    return total
# call the two functions
option_1 = option1()
option_2 = option2()
# convert option_1 to float number
option_1 = float(option_1)
print("option 1 = $" + str(round(option_1, 2)) + ".")
print("option 2 = $" + str(round(option_2, 2)) + ".")
# compare the two options
if option_1 < option_2:
    print("Option 2 is better.")
elif option_1 > option_2:
    print("Option 1 is better")
else:
    print("They are equal")
