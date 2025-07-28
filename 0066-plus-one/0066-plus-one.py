class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        resulting_array = []
        s = digits[-1] + 1
        resulting_array.append(s % 10)
        carry = s // 10
        for i in range(len(digits) - 2, -1, -1):
            s = digits[i] + carry
            resulting_array.append(s % 10)
            carry = s // 10
        
        if carry == 1:
            resulting_array.append(1)
        resulting_array.reverse()
        return resulting_array