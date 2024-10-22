# This script calculates the cost of purchasing candles based on the number of candles entered by the user.
# - If the number of candles is less than 50, the cost is $0.20 per candle.
# - If the number of candles is more than 50, the cost is $0.10 per candle.
# The total cost is printed after the calculation.

num = int(input("Enter number of candles: "))

if num <= 50:
    cost = 0.20 * num
    print("Cost is: ", cost)

else:
    cost = 0.10 * num
    print("Cost is ", cost)
