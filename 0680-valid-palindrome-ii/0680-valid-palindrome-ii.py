class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True

        l=0
        r=len(s)-1
        lst=list(s)

        while(l<r):
            lst[l],lst[r]=lst[r],lst[l]
            l+=1
            r-=1

        result="".join(lst)

        if s==result:
            return True

        else:
            l=0
            r=len(s)-1

            while(l<r):
                if s[l]!=s[r]:
                    rev=s[l+1:r+1]
                    rev2=s[l:r]

                    l=0
                    r=len(rev)-1

                    while(l<r):
                        if rev[l]!=rev[r]:
                            break
                        l+=1
                        r-=1

                    if l>=r:
                        return True

                    l=0
                    r=len(rev2)-1

                    while(l<r):
                        if rev2[l]!=rev2[r]:
                            break
                        l+=1
                        r-=1

                    if l>=r:
                        return True

                    return False

                l+=1
                r-=1
        return True
               