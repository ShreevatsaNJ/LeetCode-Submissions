class Solution:
    def reverseVowels(self, s: str) -> str:
        lst=["a","e","i","o","u"]
        l=0
        r=len(s)-1
        arr=list(s)
        while(l<=r):
            if arr[l].lower() in lst and arr[r].lower() in lst:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            elif arr[l].lower() not in lst:
                l+=1
            else:
                r-=1       
        return "".join(arr)