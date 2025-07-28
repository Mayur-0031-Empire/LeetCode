class Solution:
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def recur(index, curr_or, arr):
            # base case
            if index >= len(nums):
                arr[curr_or] += 1
                # print(arr)
                return
            # not include
            recur(index + 1, curr_or, arr)
            # include
            recur(index + 1, curr_or | nums[index], arr)
            return

        max_or_possible =(1 << (int(math.log(max(nums), 2)) + 1)) - 1

        arr = [0 for _ in range(max_or_possible + 1)]

        curr_or = 0
        recur(0, curr_or, arr)
        for i in range(1, len(arr) + 1):
            if arr[-i]:
                return arr[-i]
        
        