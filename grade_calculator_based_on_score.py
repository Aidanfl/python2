# This script calculates a letter grade based on a numeric score entered by the user.
# The user enters a score, and the script converts it to a float.
# Based on the score, it assigns a grade:
# - A for scores >= 0.9
# - B for scores >= 0.8
# - C for scores >= 0.7
# - D for scores >= 0.6
# - F for scores < 0.6
# If the score is out of range, it prints "Out of Range".
# The grade is then printed.

score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
print (x)
