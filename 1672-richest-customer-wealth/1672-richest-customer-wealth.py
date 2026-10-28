class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        lst=[]
        for i in range(len(accounts)):
            temp=0
            for j in accounts[i]:
                temp+=j
            lst.append(temp)
        max_wealth=lst[0]  
        for i in range(1,len(lst)):
            if lst[i]>max_wealth:
                max_wealth=lst[i]
        return max_wealth

                