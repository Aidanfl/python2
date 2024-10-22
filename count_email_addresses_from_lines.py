# This script reads a file, looks for lines that start with "From ", and extracts the email address from each line.
# It uses a dictionary to count how often each email address appears.
# The email address is the second word in each "From " line, and the script increments the count for that email in the dictionary.
# After processing all lines, it prints the dictionary with the count of email addresses.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Count email address

fname = input("Enter a file name: ")
fhandle = open(fname)
d = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split() # Turn the sentence into a list of words
        email = words[1]
        d[email] = d.get(email, 0) + 1
print(d)
