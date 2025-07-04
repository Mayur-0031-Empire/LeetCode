class Solution:
    def checkRecord(self, s: str) -> bool:
        return True if s.count('A') < 2 and s.count('LLL') == 0 else False