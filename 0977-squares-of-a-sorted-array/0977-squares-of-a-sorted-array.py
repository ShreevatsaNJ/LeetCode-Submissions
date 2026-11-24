class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lst=[i**2 for i in nums]
        lst.sort()
        return lst