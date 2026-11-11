class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for key,values in count.items():
            if values==1:
                return key