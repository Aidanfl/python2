# This script demonstrates how to build a dictionary from an empty dictionary.
# It starts with an empty dictionary and adds key-value pairs one by one.
# It also updates the value of an existing key ('money') by directly assigning a new value
# and then increments the value of 'money' by 20.
# The dictionary is printed after each modification.

# Build a dictionary below from an empty dictionary
# d = {'money': 20, 'candy': 3, 'pen': 3}
d = {} # d = dict() define an empty dictionary
print(d)
d['money'] = 20
print(d)
d['candy'] = 3
print(d)
d['pen'] = 3
print(d)
d['money'] = 50
print(d)
d['money'] = d['money'] + 20
print(d)
