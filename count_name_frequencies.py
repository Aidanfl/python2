# This script counts the frequencies of each name in a list and stores the results in a dictionary.
# It uses the names as keys and their frequencies as values.
# The dictionary is updated as the script loops through the list of names, printing the updated dictionary after each addition or update.

names = ['csev', 'cwen', 'csev', 'sqian', 'cwen']
# Count the frequencies of each name in the list
# and save the name and their frequencies in a dictionary
# use names as keys and their frequencies as values
# Loop through the names in the list
d = {}

for name in names:
    if name not in d: # If the name is not in the dictionary
        d[name] = 1   # assign 1 to this name, add the name to the dictionary
    else:
        d[name] = d[name] + 1
                    # If the name is in the dictionary, update its value
    print(d)
