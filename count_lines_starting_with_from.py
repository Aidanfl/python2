# This script reads through a file and counts how many lines start with "From:".
# It prints the total count of such lines.
# You can test it with files like "mbox.txt" or "mbox-short.txt".

#if a line starts with "From:", display the line
#(test mbox.txt, and mbox-short.txt)
handle = open("mbox-short.txt")
for line in handle: # loop through the file line by line
    if line.startswith("From:"):
        count = count + 1
print(count)
