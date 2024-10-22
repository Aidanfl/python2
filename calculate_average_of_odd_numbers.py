# This script reads numbers from a file named 'Numbers.txt' and collects all odd numbers into a list.
# It defines a function `readFile(file)` that opens the file, checks each number,
# and appends the odd numbers to the list. The script then calculates the average of the odd numbers
# using the sum() and len() functions, and prints the result.

def readFile(file):
    odds = []
    with open(file, 'r') as fhandle:
        for line in fhandle:
            number = int(line.strip())
            if number % 2 != 0:
                odds.append(number)
    return odds

file = 'Numbers.txt'
odds = readFile(file)
if len(odds) > 0:
    average = sum(odds) / len(odds)
    print(f"The average of all odd numbers in this list is: {average}")
