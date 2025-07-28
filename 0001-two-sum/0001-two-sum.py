class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in present:
                return [present[t], i]
            present[nums[i]] = i
        return [-1, -1]
        
        

