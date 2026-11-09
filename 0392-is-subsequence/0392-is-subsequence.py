class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        for i in range(len(s)):
            if s[i] in t:
                count+=1
                t=t[t.find(s[i])+1 : ]
        if count==len(s):
            return True
        return False