class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        goback = start
        gofront = start

        def check(index):
            if 0 <= index and index < len(nums):
                return True
            else :
                return False

        while(check(goback) or check(gofront)):
            if check(goback):
                if nums[goback] == target:
                    return abs(goback - start)
            
            if check(gofront):
                if nums[gofront] == target:
                    return abs(gofront - start)
            
            goback -= 1
            gofront += 1
        
        return -1
                
        