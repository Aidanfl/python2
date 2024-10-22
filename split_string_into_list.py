# This script demonstrates how to split a string into a list using the split() method.
# It takes a string 'state' with the value "New York,NY,Empire State,Albany" and splits it by commas.
# The result is stored in 'stateFacts', which is a list containing each part of the original string, and the list is printed.

state = "New York,NY,Empire State,Albany"
stateFacts = state.split(',')
print(stateFacts)
