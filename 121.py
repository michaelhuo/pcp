class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        prev_price = prices[0]
        min_price = prev_price
        for price in prices[1:]:
            if price < prev_price:
                profit = prev_price - min_price
                if profit > max_profit:
                    max_profit = profit
                if price < min_price:
                    min_price = price
            prev_price = price
        profit = prev_price - min_price
        if profit > max_profit:
            max_profit = profit
        return max_profit
            
