# This script demonstrates how to sort the elements of a tuple.
# Since tuples are immutable, the tuple 'nums' is first converted to a list, sorted, and then converted back to a tuple.
# The sorted tuple is then printed.

nums = (1, 2, 8, 6)

# Convert the tuple to a list
nums_list = list(nums)

# Sort the list
nums_list.sort()

# Convert the list back to a tuple if needed
sorted_nums = tuple(nums_list)

# Print the sorted tuple
print(sorted_nums)
