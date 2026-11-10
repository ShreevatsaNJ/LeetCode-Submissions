class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        count = 0
        while num > 0:
            lastDigit = num % 10
            count += lastDigit
            num //= 10
            
        while count >= 10:
            total = 0
            while count > 0:
                lastDigit = count % 10
                total += lastDigit
                count //= 10
            count = total
        return count

