class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        arr=[]
        if len(nums)==1 or k==0:
            pass
        else:
            k=k%len(nums)
            if k==0:
                return
            for i in range(len(nums)-k,len(nums)):
                arr.append(nums[i])
            nums[:]=arr[:]+nums[:-k]
            


