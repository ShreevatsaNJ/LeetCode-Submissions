class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        for i in range(len(s)):
            if s[l]!=s[r]:
                new_s=s[:l]+s[l+1:]
                new_s2=s[:r]+s[r+1:]

                if new_s==new_s[::-1]:
                    return True

                if new_s2==new_s2[::-1]:
                    return True

                return False

            l+=1
            r-=1

        return True
               