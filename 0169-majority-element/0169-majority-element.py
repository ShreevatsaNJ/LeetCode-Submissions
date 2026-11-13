class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        max_value=count[nums[0]]
        for key,value in count.items():
            if count[key]>=max_value:
                max_value=count[key]
                ans=key
        return ans

            