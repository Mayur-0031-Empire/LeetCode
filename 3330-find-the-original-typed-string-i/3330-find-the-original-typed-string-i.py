class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]
        possible_string_count = 0
        for ch in word :
            if ch == prev:
                possible_string_count += 1
            prev = ch
        return possible_string_count