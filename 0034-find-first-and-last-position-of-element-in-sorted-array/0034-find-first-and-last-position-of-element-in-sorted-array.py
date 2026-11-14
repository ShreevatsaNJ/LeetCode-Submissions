class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        f=0
        l=len(nums)-1
        first=-1

        last=-1

        while(f<=l):
            mid=(f+l)//2
            if target>nums[mid]:
                f=mid+1
            elif target<nums[mid]:
                l=mid-1
            else:
                first=mid
                l=mid-1

        f=0
        l=len(nums)-1

        while(f<=l):
            mid=(f+l)//2
            if target>nums[mid]:
                f=mid+1
            elif target<nums[mid]:
                l=mid-1
            else:
                last=mid
                f=mid+1

        return [first,last]