class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        num1 = 0
        num2 = 0

        multiplier = 1
        while n > 0 :
            last_digit = n % 10
            if last_digit > 1:
                num1 += (1 * multiplier)
                num2 += (last_digit - 1) * multiplier
            elif n < 2:
                num1 += (n * multiplier)
                return [num1, num2]
            else :
                num1 += (2 * multiplier)
                n = n - 2
                num2 += (n % 10) * multiplier
            n //= 10
            multiplier *= 10
        
        return [num1, num2]
