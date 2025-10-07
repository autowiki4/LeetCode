class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            curr = p-min_price
            max_profit = max(curr, max_profit)
        return max_profit
        