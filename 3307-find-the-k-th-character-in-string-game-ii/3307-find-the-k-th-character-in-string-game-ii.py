class Solution:
    def recur(self, k, op):
        if k == 1:
            return 0
        jump = 0  # power of 2
        num = 1  # value of that power of 2
        while num < k:
            num <<= 1
            jump += 1
        affecting_character = k - (1 << (jump - 1))
        return op[jump - 1] +  self.recur(affecting_character, op)
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count = self.recur(k ,operations)

        ans = chr((count % 26) + ord('a'))
        return ans