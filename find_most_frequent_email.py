# This script reads through a file, identifies lines that start with "From ", and extracts the email address from each line.
# It counts how many times each email address appears and then identifies the email address with the highest count.
# Enter the file name, and the script will display the most frequent email address and how many times it appears.

fhandle = input("Enter a file name: ")
f = open(fhandle)

counts = dict() # Counts is the name of a newly-made, empty dictionary


for line in f:
    if line.startswith("From "):
        words = line.split() # Splits each line into individual words
        email = words[1] # Shortens each split line into just the second word of each line (starts at 0)
        counts[email] = counts.get(email, 0) + 1 # Counts how many emails for each person starting with 0 +1 for each instance shown

maxC = 0
maxE = None

for email, count in counts.items():
    if count > maxC:
        maxC = count
        maxE = email

print(maxE, maxC)
