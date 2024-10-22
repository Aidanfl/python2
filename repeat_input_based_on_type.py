# This script asks the user for input 5 times in a loop.
# Depending on the context:
# 1. If working with numbers: it multiplies the input by 2 and prints the result.
# 2. If working with strings: it repeats the string twice and prints the result.

for i in range(1, 6):
    s = float(input("Enter a number: "))  # Prompt reflects a number
    s = s * 2
    print(s)
