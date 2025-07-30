class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # print(s)
        new_s = []
        for ch in s:
            if "0" <= ch <= "9" or "a" <= ch <=  "z":
                new_s.append(ch)
        i = 0
        j = len(new_s) - 1
        # print(''.join(new_s))
        while i < j:
            # print(s[i], s[j])
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        return True
