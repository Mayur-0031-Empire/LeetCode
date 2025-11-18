class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ans = [bit for bit in bits[::-1]]
        while len(ans) > 1:
            if ans[-1] == 0:
                ans.pop()
            if ans[-1] == 1:
                ans.pop()
                ans.pop()
        if len(ans) == 0:
            return False
        elif len(ans) == 1:
            return True
        else :
            return False