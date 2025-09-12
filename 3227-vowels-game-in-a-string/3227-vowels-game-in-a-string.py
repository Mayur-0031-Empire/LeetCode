class Solution:
    def doesAliceWin(self, s: str) -> bool:
        present = ["a", "e", "i", "o", "u"]
        for ch in s:
            if ch in present:
                return True
        return False