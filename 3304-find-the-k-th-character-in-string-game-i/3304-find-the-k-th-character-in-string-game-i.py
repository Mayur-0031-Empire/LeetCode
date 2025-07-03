class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        while len(word) <= k:
            for i in range(len(word)):
                word.append(chr(ord(word[i]) + 1))
        return word[k - 1]