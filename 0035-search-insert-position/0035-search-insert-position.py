class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = end + 1
        while start <= end:
            mid = start + (end - start)//2

            if target == nums[mid]:
                ans = mid
                end = mid - 1
            elif target < nums[mid]:
                ans = mid
                end = mid - 1
            else :
                start = mid + 1
        
        return ans
            
