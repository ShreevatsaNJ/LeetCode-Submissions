class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        count={}
        for i in range(len(nums)):
            if nums[i] in count:
                if abs(count[nums[i]]-i)<=k:
                    return True
                else:
                    count[nums[i]]=i
            else:
                count[nums[i]]=i    
        return False