class Solution:
    def maxSum(self, nums: List[int]) -> int:
        present = [0 for i in range(202)]
        for num in nums:
            num += 100
            present[num] += 1
        max_sum = 0
        for i in range(101, 201):
            if present[i]:
                max_sum += i - 100
        # print(present)
        if max_sum == 0:
            for i in range(100, -1, -1):
                # print(present[i])
                if present[i]:
                    return (i- 100)
        return max_sum

        