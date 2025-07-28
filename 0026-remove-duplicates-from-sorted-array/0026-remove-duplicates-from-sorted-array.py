class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[curr_index] = nums[i]
                curr_index += 1
        return curr_index
        