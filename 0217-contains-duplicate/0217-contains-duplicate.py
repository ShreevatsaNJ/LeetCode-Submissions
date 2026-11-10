class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for key,values in count.items():
            if count[key]>1:
                return True 
        return False