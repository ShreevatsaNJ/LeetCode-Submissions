class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count={}
        for i in s:
            if i in count:
                count[i]+=1
                if count[i]>=2:
                    return i
                    break
            else:
                count[i]=1
            