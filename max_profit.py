class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_at = prices[0]
        profit = 0
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[i] < buy_at:
                buy_at = prices[i] 
            else:
                profit = prices[i] - buy_at
                max_profit = max(profit,max_profit)
        return max_profit
        
            