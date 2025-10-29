class Solution:
    def smallestNumber(self, n: int) -> int:
        a = 0
        while n > 0:
            a = (a << 1) + 1
            n >>= 1
        return a
        