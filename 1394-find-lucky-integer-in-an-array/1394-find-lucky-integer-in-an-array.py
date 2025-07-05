class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0 for _ in range(501)]
        for num in arr:
            freq[num] += 1
        freq[0] = -1
        lucky_integer = -1
        for f, i in enumerate(freq):
            if i == f:
                lucky_integer = i
        
        return lucky_integer