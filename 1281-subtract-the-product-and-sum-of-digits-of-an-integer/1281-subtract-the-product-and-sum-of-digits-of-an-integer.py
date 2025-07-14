class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sumOfDigit = 0
        while n:
            digit = n % 10
            product *= digit
            sumOfDigit += digit
            n//=10
        return product - sumOfDigit