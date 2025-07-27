class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills_and_valleys = [nums[0]]
        for num in nums:
            if hills_and_valleys[-1] != num:
                hills_and_valleys.append(num)
        
        count = 0
        for i in range(1, len(hills_and_valleys) - 1):
            if hills_and_valleys[i - 1] < hills_and_valleys[i] > hills_and_valleys[i + 1]:
                count += 1
            if hills_and_valleys[i - 1] > hills_and_valleys[i] < hills_and_valleys[i + 1]:
                count += 1
        
        return count