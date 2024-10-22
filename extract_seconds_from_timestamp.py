# This script extracts and displays the seconds from a timestamp in a given string.
# It splits the string into words, retrieves the time portion, and then splits the time into hours, minutes, and seconds.
# The script prints only the seconds part of the time.

s = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# Turn the strig into a list of words (seperated by white space(s))
words = s.split()
# Words = ["From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
time = words[5] # Time = "09:14:16"
parts = time.split(":") # Parts = ["09", "14", "16"]
second = parts[2]
print(second)
