class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lst=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                lst.append(True)
            else:
                lst.append(False)
        return lst