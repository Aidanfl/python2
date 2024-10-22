# This script calculates the frequencies of words in a text file.
# Enter the name of the text file, and the script will read the file line by line,
# split each line into words, and count how many times each word appears.
# The results are stored in a dictionary where the key is the word and the value is its frequency.

fname = input("Enter a text file name: ")
fhandle = open(fname)

d = dict()
# Read the file line by line, each line is a sentence
for line in fhandle:
    lst =  line.split() # Lst is a list containing all words form the line
    for item in lst:
        d[item] = d.get(item, 0) + 1
