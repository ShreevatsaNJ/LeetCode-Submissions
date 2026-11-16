class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total=0
        for i in stones:
            if i in jewels:
                total+=1
        return total