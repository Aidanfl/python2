# This script finds and displays the most common name in a given list of names.
# It first calculates the frequency of each name and then identifies the name with the highest frequency.
# The most common name and its frequency are printed.

# Find the most common name in the list
names = ["csev", "cwen", "csev", "zqian", "cwen"]
# Calculate the frequencies of names
d = dict()
for name in names:
    d[name] = d.get(name, 0) + 1
# Find the name with the highest frequency from the dictionary d
highestFrequency = None
highestName = None
for name, fre in d.items():
    if highestFrequency is None:
        highestFrequency = fre
        highestName = name
    elif highestFrequency < fre:
        highestFrequency = fre
        highestName = name

print("The most common name:", highestName)
print("The frequency of the most common name:", highestFrequency)
