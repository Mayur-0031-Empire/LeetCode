class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_index = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[curr_index] = nums[i]
                curr_index += 1
        
        while curr_index < len(nums):
            nums[curr_index] = 0
            curr_index += 1
        return 

        