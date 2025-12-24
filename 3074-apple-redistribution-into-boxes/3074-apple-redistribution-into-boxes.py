class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total_box_needed = 0
        current_capacity = 0
        total = sum(apple)
        # print(capacity)
        for c in capacity:
            current_capacity += c
            total_box_needed += 1
            if current_capacity >=  total:
                return total_box_needed
        return total_box_needed

        