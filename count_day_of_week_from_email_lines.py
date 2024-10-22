# This script reads a file, looks for lines that start with "From ", and extracts the day of the week from each line.
# It uses a dictionary to count how often each day of the week appears.
# The day is the third word in each "From " line, and the script increments the count for that day in the dictionary.
# After processing all lines, it prints the dictionary with the count of days.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
fname = input("Enter a file name: ")
fhandle = open(fname)
d = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split() # Turn the sentence into a list of words
        day = words[2]
        d[day] = d.get(day, 0) + 1
print(d)
