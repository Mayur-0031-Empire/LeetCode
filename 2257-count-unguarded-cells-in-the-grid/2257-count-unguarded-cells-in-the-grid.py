class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        resultant_grid = [[0 for _ in range(n)] for _ in range(m)]
        guard = 2
        wall = 3
        # if not guarded = 0
        guarded = 1
        not_guarded = 0
        rows = m
        cols = n
        for g in guards:
            r, c = g
            resultant_grid[r][c] = 2
        for w in walls:
            r, c = w
            resultant_grid[r][c] = 3
        
        for i, row in enumerate(resultant_grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    r = i - 1
                    c = j
                    # up
                    while r >= 0 and resultant_grid[r][c] != wall and resultant_grid[r][c] != guard:
                        resultant_grid[r][c] = guarded
                        r -= 1
                    # down
                    r = i + 1
                    c = j
                    while r < rows and resultant_grid[r][c] != wall and resultant_grid[r][c] != guard:
                        resultant_grid[r][c] = guarded
                        r += 1

                    # left
                    r = i
                    c = j - 1
                    while c >= 0 and resultant_grid[r][c] != wall and resultant_grid[r][c] != guard:
                        resultant_grid[r][c] = guarded
                        c -= 1
                    # right
                    r = i
                    c = j + 1
                    while c < cols and resultant_grid[r][c] != wall and resultant_grid[r][c] != guard:
                        resultant_grid[r][c] = guarded
                        c += 1

        ans = 0
        for row in resultant_grid:
            for cell in row:
                if cell == not_guarded:
                    ans += 1
        return ans
