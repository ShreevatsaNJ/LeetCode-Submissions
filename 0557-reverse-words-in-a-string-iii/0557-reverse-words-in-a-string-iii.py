class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        lst2=[]
        for i in lst:
            temp=i
            arr=list(temp)   
            l=0
            r=len("".join(arr))-1
            while(l<=r):
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            lst2.append("".join(arr))
        result=" ".join(lst2)
        return result