class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        else:
            while n%3==0:
                n=n//3
            if n==1:
                return True
            else:
                return False