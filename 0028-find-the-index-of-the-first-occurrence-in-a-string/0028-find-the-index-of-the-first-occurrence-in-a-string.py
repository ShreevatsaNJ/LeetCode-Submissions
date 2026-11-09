class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        r=0
        start=0
        while(l<len(needle) and r<len(haystack)):
            if needle[l]==haystack[r]:
                l+=1
                r+=1
            else:
                start+=1
                l=0
                r=start
        return r-len(needle) if l==len(needle) else -1 