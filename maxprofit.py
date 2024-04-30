def max_profit(stock_prices):
    if not stock_prices or len(stock_prices) < 2:
        return 0
    
    min_price = stock_prices[0]
    max_profit = 0
    
    for price in stock_prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit

stock_prices = [10, 7, 5, 8, 11, 9]
print(max_profit(stock_prices))