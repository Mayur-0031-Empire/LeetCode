class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bit_array = [-1 for _ in range(32)]
        ans = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            for bit in range(32):
                if (nums[i] & (1 << bit)):
                    bit_array[bit] = i
            # print(bit_array[:4])
            
            max_index = max(bit_array)
            ans[i] = max_index - i + 1
        
        return ans
