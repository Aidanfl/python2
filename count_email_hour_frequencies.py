# This script reads a file and counts how frequently each hour appears in lines that start with "From ".
# It extracts the time from each relevant line, splits the time to get the hour, and builds a dictionary where the hour is the key and its frequency is the value.
# The dictionary is then converted into a list of tuples (hour, frequency), sorted by hour in ascending order.
# Finally, it prints each hour and its corresponding frequency.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Open a file
fname = input("Enter a file name:")
fhadle = open(fname)

# Build a dictionary with horus as keys and their frequencies as values
d = {}
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        parts = time.split(":")
        hour = parts[0]
        d[hour] = d.get(hour, 0) + 1

# Generate a list of tuples in the form of (hour, frequency)
lst = d.items()

# Sort the list by hour in ascending order
lst = sorted(lst)

# Display hours and their frequencies
for hour, fre in lst:
    print(hour, fre)
