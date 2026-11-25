class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared=[i**2 for i in nums]
        squared.sort()
        return squared