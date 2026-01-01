class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            sum = digits[i] + carry 
            digit = (sum) % 10
            result.append(digit)
            carry = sum // 10
        if carry == 1:
            result.append(carry)
        result.reverse()
        return result
        