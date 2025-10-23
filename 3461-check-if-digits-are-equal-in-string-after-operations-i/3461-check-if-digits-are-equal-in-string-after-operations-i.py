class Solution:
    def hasSameDigits(self, s: str) -> bool:
        ans = [int(digit) for digit in s]
        while len(ans) > 2:
            for i in range(len(ans) - 1):
                ans[i] = (ans[i] + ans[i + 1]) % 10
            ans.pop()
        return ans[0] == ans[1]
        