from collections import defaultdict

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] == 1:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if i < m - 1:
                memo[(i, j)] += dfs(i + 1, j)
            if j < n - 1:
                memo[(i, j)] += dfs(i, j + 1)
            return memo[(i, j)]

        memo = defaultdict(int)
        return dfs(0, 0)