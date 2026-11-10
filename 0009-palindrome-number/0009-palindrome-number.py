class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst=[]
        temp=x
        i=0
        while i<=len(str(temp))-1:
            lastDigit=x%10
            lst.append(lastDigit)
            x//=10
            i+=1
        arr=[str(i) for i in lst]
        if int ("".join(map(str,arr)))==temp:
            return True
        return False
        