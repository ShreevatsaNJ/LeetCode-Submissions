class Solution:
    def repeatedCharacter(self, s: str) -> str:
        total={}
        for i in s:
            if i in total:
                total[i]+=1
                if total[i]>=2:
                    return i
                    break
            else:
                total[i]=1
            