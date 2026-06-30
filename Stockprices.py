def maxProfit(prices):
    min_price = float('inf')   # track lowest price so far
    max_profit = 0             # track best profit so far

    for price in prices:
        if price < min_price:
            min_price = price          # found a cheaper buy day
        elif price - min_price > max_profit:
            max_profit = price - min_price   # better profit found

    return max_profit

# Test
print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(maxProfit([7, 6, 4, 3, 1]))     # 0