class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lst=[]
        max_value=candies[0]
        for i in range(1,len(candies)):
            if candies[i]>max_value:
                max_value=candies[i]
        for i in candies:
            if i+extraCandies>=max_value:
                lst.append(True)
            else:
                lst.append(False)
        return lst