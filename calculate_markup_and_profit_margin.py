# This script calculates the markup, percentage markup, and profit margin based on the purchase price and selling price.
# Enter the purchase price and selling price when prompted.
# The script will display the markup, the percentage markup relative to the purchase price, and the profit margin relative to the selling price.

purchaseprice = float(input("Enter purchase price: "))
sellingprice = float(input("Enter selling price: "))

markup = sellingprice - purchaseprice
percentagemarkup = markup / purchaseprice * 100
profitmargin = markup / sellingprice * 100

print("Markup: ", markup)
print("Percentage markup: ", percentagemarkup, "%")
print("Profit margin: ", round(profitmargin, 2), "%")
