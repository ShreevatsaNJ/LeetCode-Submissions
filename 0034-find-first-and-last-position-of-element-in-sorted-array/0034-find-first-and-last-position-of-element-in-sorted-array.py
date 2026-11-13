class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l=0
        r=len(nums)-1
        first=-1
        last=-1

        while(l<=r):
            mid=(l+r)//2
            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                first=mid
                r=mid-1

        l=0
        r=len(nums)-1

        while(l<=r):
            mid=(l+r)//2
            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                last=mid
                l=mid+1

        return [first,last]