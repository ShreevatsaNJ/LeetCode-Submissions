class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        temp = list(strs[0])

        for i in strs[1:]:
            if len(i) == 0:
                return ""

            x = min(len(i), len(temp))
            j = 0

            while j < x:
                if temp[j] != i[j]:
                    temp = temp[:j]
                    break
                j += 1

            if len(i) < len(temp):
                temp = list(i)

        return "".join(temp)