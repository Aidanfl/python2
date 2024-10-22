# This script reads a file and filters lines that start with "From ".
# It extracts the email address from each of these lines, retrieves the domain (host name),
# and prints the domain. Additionally, it counts how many times "umich.edu" appears as a domain.
# Enter the file name, and the results will be displayed.

fname = input("Enter the file name: ")
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From "):
    # Turn the string into a list of words (seperated by white space(s))
    words = line.split()
    # Words=["From", "stephen.marquard@utc.ac.za", "Sat", "Jan", "5", "09:14:16"]
    email = words[1] #
    parts = email.split ("@") # Parts = ["stephen.marquard", "utc.ac.za"]
    domain = parts[1]
    print(domain)
    ifdomain == "umich.edu":
        count = count + 1
pprint("umich.edu appears", count, "time.")
