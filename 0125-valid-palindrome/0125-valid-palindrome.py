class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for ch in s:
            if ch.isalnum():
                temp+=ch.lower()
        result=list(temp.replace(" ",""))
        l=0
        r=len(result)-1
        if len(s)<=1:
            return True
        while(l<=r):
            result[l],result[r]=result[r],result[l]
            l+=1
            r-=1
        if "".join(result)==temp:
            return True 
        return False
