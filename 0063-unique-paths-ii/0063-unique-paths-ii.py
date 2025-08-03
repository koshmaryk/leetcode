class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return 0
    
        grid[0][0] = 1
        
        for i in range(1, m):
            grid[i][0] = int(grid[i - 1][0] == 1 and grid[i][0] == 0)

        for j in range(1, n):
            grid[0][j] = int(grid[0][j - 1] == 1 and grid[0][j] == 0)

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
        return grid[m - 1][n - 1]