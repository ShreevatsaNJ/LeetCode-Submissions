class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        key=list(s)
        value=list(t)
        count={}
        total={}

        for i in range(len(key)):
            if key[i] in count and count[key[i]]!=value[i]:
                return False
            if value[i] in total and total[value[i]]!=key[i]:
                return False

            count[key[i]]=value[i]
            total[value[i]]=key[i]

        return True

            
                 