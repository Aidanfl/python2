# This script continuously prompts you to enter numbers and calculates the total, count, average, and maximum value.
# You can enter numbers as many times as you want, and type 'done' when you're finished.
# It will handle invalid input gracefully and provide the results once you stop entering numbers.

count = 0
total = 0
maximum = None

while True:
    num = input("Enter a number, or 'done' to exit: ")
    if num == "done":
        break
    
    try:
        number = float(num)
    except ValueError:
        print("Invalid input")
        continue
    
    count += 1
    total += number
    
    if maximum is None or number > maximum:
        maximum = number
    
if count > 0:
    average = total / count
    print("Total: ",(total))
    print("Count: ",(count))
    print("Average: ",(average))
    print("Maximum: ",(maximum))
