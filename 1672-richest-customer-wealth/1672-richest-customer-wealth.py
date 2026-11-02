class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        total_wealth=[]
        for i in range(len(accounts)):
            temp=0
            for j in accounts[i]:
                temp+=j
            total_wealth.append(temp)
        max_wealth=total_wealth[0]  
        for i in range(1,len(total_wealth)):
            if total_wealth[i]>max_wealth:
                max_wealth=total_wealth[i]
        return max_wealth

                