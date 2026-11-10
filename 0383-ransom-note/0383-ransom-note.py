class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i=0
        count=0
        lst=list(ransomNote)
        arr=list(magazine)
        while (i<=len(lst)-1):
            if lst[i] in arr:
                arr.remove(lst[i])
                count+=1
            i+=1
        if count==len(lst):
            return True
        return False
                
            
            

