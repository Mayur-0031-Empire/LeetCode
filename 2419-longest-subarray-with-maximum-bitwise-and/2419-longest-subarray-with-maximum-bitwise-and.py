class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        i = 0
        j = 0
        n = len(nums)
        ans = 1
        while j < n:
            if nums[j] != max_val:
                # print(ans)
                j += 1
                i = j
            else :
                ans = max(ans, j - i + 1)
                j += 1
        return ans