class Solution:
    def isvalid(self, set1, set2):
        count = 0
        for i in range(26):
            if set1[i] != set2[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        present1 = [0 for _ in range(26)]
        present2 = [0 for _ in range(26)]
        
        for ch in s1:
            present1[ord(ch) - ord('a')] += 1
        for ch in s2[:len(s1)]:
            present2[ord(ch) - 97] += 1
        if self.isvalid(present1, present2):
            return True
        i = 0
        j = len(s1)
        while j < len(s2):
            ch1_index = ord(s2[i]) - 97
            ch2_index = ord(s2[j]) - 97
            present2[ch1_index] -= 1
            i += 1
            present2[ch2_index] += 1
            j += 1
            if self.isvalid(present1, present2):
                return True
        
        return False
