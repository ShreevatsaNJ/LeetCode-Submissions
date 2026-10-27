class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in range(len(nums)):
            if i==0:
                lst.append(nums[i])
            else:
                lst.append(nums[i]+lst[i-1])
        return lst
      
        
        
    