class Solution:
    def check(self, nums: List[int]) -> bool:
        
        i = 1
        n = len(nums)
        while i < n:
            if nums[i - 1] <= nums[i]:
                i += 1 
            else:
                break
        if i == n:
            return True
        nums[i:] = nums[i:][::-1]
        nums[:i] = nums[:i][::-1]
        nums[:] = nums[:][::-1]
        i = 1
        while i < n:
            if nums[i - 1] <= nums[i]:
                i += 1
            else :
                return False
        return True