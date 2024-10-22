# This script compares two salary options over the next ten years.
# Option 1 starts at $20,000 per year with a raise of $1,000 at the end of each year.
# Option 2 starts at $10,000 per half-year with a raise of $250 at the end of each half-year.
# The script calculates the total earnings for each option and prints the results.

# Option 1: $20,000 per year, with a raise of $1,000 at the end of each year
salary1 = 20000
raise1 = 1000
total1 = 0

# Option 2: $10,000 per half-year, with a raise of $250 per half-year at the end of each half-year
salary2 = 10000
raise2 = 250
total2 = 0
# Calculate the total earnings for each option over the next ten years

for year in range(1, 11):
    total1 = total1 + salary1
    salary1 = salary1 + raise1

for year in range(1, 21):
    total2 = total2 + salary2
    salary2 = salary2 + raise2


print("Option 1 earns $", (total1))

print("Option 2 earns $", (total2))
