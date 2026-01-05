class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # find total absolute sum, minimum number, total number of -tive signs 
        total_sum = 0
        minimum_num = abs(matrix[0][0])
        total_negative = 0
        zero_exits = 0
        for row in matrix:
            for cell in row:
                if cell < 0 :
                    total_negative += 1
                
                if cell == 0:
                    zero_exits = 1
                
                if minimum_num > abs(cell):
                    minimum_num = abs(cell)
                total_sum += abs(cell)
        # print(total_sum)
        if zero_exits or total_negative % 2 == 0:
            return total_sum
        total_sum -= (2 * minimum_num)
        # print(total_sum)
        return total_sum