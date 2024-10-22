# This script prompts the user to enter a file name, reads through the file, and looks for lines that start with "X-DSPAM-Confidence:".
# It extracts the floating-point number from each of these lines and calculates the average of all the spam confidence values.
# The script keeps track of the count of these lines and the total of the spam confidence values.
# Finally, it prints the average spam confidence rounded to 12 decimal places.

# Write a program to prompt for a file name
fname = input("Enter a file name: ")
# Open the file
fhandle = open(fname)
# Read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
count = 0 # track line numbers
total = 0 # keep the total of all numbers read so far
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull
# apart the line to extract the floating-point number on the line.
        position_colon = line.find(":")# find the position of ":"
        portion = line[ position_colon + 1 :   ]
        number = float(portion)

# Count these lines
        count = count + 1
# compute the total of the spam confidence values
        total = total + number
# Print out the average spam confidence
print("Average spam confidence: ", round(total/count, 12))
