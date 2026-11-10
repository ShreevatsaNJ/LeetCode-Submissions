class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while i>=0:
            if i*i==x:
                return i
                break
            elif i*i>x:
                return i-1
                break
            else:
                i+=1