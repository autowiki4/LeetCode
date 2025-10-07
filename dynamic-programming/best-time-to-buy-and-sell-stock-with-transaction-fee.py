class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        hold = -prices[0]
        cash = 0
        
        for i in range(1, n):
            new_hold = max(hold, cash - prices[i])
            new_cash = max(cash, hold + prices[i] - fee)
            
            hold, cash = new_hold, new_cash
        
        return cash 