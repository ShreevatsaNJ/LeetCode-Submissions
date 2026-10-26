class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:    
        str1="".join(map(str,digits))
        lst=int(str1)
        temp=lst+1
        str2=str(temp)
        lst1=[]
        for ch in str2:
            lst1.append(int(ch))
        return lst1 