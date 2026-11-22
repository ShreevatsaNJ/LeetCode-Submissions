class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        total = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_val = nums[i] + nums[left] + nums[right]
                if total_val == 0:
                    total.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif total_val < 0:
                    left += 1
                else:
                    right -= 1
        return total