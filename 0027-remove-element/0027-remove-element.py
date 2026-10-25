class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=len(nums)
        for i in range(k-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)
        return len(nums)