class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_value=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<=min_value:
                min_value=prices[i]
            value=prices[i]-min_value
            if value>=max_profit:
                max_profit=value
        if max_profit>0:
            return max_profit  
        else:
            return 0