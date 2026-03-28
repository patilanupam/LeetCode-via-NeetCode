def maxProfit(prices):
    min_price = float('inf')  
    # thinking: start with worst possible (very high), so first real price replaces it

    max_profit = 0  

    for price in prices:
        # update minimum buying price seen so far
        if price < min_price:
            min_price = price

        # if we sell today, what's the profit?
        profit = price - min_price

        # keep track of best profit seen so far
        if profit > max_profit:
            max_profit = profit

    return max_profit

# Time Complexity: O(n) - we go through the list once
# Space Complexity: O(1) - we only use a few variables, no extra space