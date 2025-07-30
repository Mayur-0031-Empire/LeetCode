class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while len(s) and part in s:
            print(s)
            s = s.replace(part, "", 1)
        return s