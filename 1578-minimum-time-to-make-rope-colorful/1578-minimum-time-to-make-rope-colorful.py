class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) <= 1:
            return 0
        start = 0
        end = 1
        # calculate_max_value remove all the remaining lesser value
        min_time = 0
        while end < len(colors):
            if colors[start] == colors[end]:
                while (end + 1) < len(colors) and colors[start] == colors[end + 1]:
                    end += 1
                total_sum = sum(neededTime[start: end + 1])
                stay_color = max(neededTime[start: end + 1])
                min_time += total_sum - stay_color
            start = end
            end += 1
        return min_time