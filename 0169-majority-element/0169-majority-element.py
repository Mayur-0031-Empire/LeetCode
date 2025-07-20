class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                ans = num
            if ans == num:
                count += 1
            else :
                count -= 1
        return ans
            