class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_value=prices[0]
        max_value=0
        for i in range(1,len(prices)):
            if prices[i]<=min_value:
                min_value=prices[i]
            value=prices[i]-min_value
            if value>=max_value:
                max_value=value
        if max_value>0:
            return max_value   
        else:
            return 0