# This script checks if the number 43 is in a given list of numbers.
# If 43 is found, it prints "Found" and stops the loop.
# If 43 is not found after checking the entire list, it prints "Not found".

# check if 43 is in the list or not, if it is,
# display found, else, display not found

found = False # not found

for num in [6,7,43,-5,0]:
    if num == 43:
        print("Found")
        found = True # it is found
        break

if found == False:
    print("Not found")
