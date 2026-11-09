class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        total={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for j in t:
            if j in total:
                total[j]+=1
            else:
                total[j]=1
        if count==total:
            return True
        return False
