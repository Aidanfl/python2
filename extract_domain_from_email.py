# This script extracts and displays the domain (host name) from an email address in a given string.
# It splits the string into words, retrieves the email address, and then splits the email at the "@" symbol.
# The script prints the domain part of the email address.

s = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# Turn the strig into a list of words (seperated by white space(s))
words = s.split()
# Words = ["From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
email = words[1]
parts = email.split ("@") # Parts = ["stephen.marquard", "utc.ac.za"]
domain = parts [1]
print(domain)
