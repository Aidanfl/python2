# This script reads a file specified by the user and counts the frequency of each word.
# It creates a dictionary to store each word as a key and its count as the value.
# After processing all lines in the file, it finds and prints the word that appears most frequently along with its count.
# The script handles cases where words may have different occurrences by using the get() method for dictionaries.

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
