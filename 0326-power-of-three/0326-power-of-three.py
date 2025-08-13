class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a = 1
        if  n <= 0:
            return False
        if n == 1:
            return True
        while a < n:
            a *= 3
            if a == n:
                return True
        
        return False
        