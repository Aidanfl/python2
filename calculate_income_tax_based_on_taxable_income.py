# This script calculates the tax based on the user's taxable income.
# The user inputs their taxable income, and the tax is calculated as follows:
# - If the income is less than or equal to $20,000, the tax is 2% of the income.
# - If the income is between $20,001 and $50,000, the tax is $400 plus 2.5% of the amount over $20,000.
# - If the income is more than $50,000, the tax is $1,150 plus 3.5% of the amount over $50,000.
# The calculated tax is displayed as an integer.

taxableIncome = int(input("Enter your Taxable Income: "))

# if taxableIncome is less than or equal to 20000, then
# calculate tax as .02 * taxableIncome.
if(taxableIncome <= 20000):
    tax = .02 * taxableIncome
# if taxableIncome is more than 20000 , then
# execute this else block.
else:
    # if taxableIncome is less than or equal to 50000, then
    # calculate tax as 400 + .025*(taxableIncome - 20000).
    if(taxableIncome <= 50000):
        tax = 400 + .025 *(taxableIncome - 20000)
    # if taxableIncome is more than 50000, then
    # calculate tax as 1150 + .035*(taxableIncome - 50000).
    else:
        tax = 1150 + .035 *(taxableIncome - 50000)
        
# Display tax applicable on given taxableIncome..
# As tax is to be displayed in integer format, 
# so cast it into integer using int() function.
print("Your Tax is: $",int(tax)) 
