class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        else:
            while n % 2==0:
                n=n//2
            if n==1:
                return True
            
        return False