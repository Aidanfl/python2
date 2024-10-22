# This script prints "Hello World" 100 times, each time displaying the line number along with the message.
# It uses a while loop, starting from 100 and counting down to 0.
# After printing the message 100 times, it prints "Done".

n = 100 # n is an iteration variable, 1 is the initial value

while n >= 0: # termination condition
    print(n, "Hello World")
    n = n - 1 # update statement
print("Done")
