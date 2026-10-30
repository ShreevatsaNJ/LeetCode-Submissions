class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_value,right_value=0,0
        total=sum(nums)
        for i in range(len(nums)):
            pivot=i
            if pivot==0:
                left_value=0
            else:
                left_value=left_value+nums[pivot-1]
            right_value=total-nums[pivot] -left_value
            if left_value==right_value:
                return pivot
        return -1


            





            
