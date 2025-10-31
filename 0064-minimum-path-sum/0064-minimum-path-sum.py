class Solution:
    '''
    [1,3,1],
    [1,5,1],
    [4,2,1]

    [0,0,0],
    [0,0,0],
    [0,0,1]

    dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])

    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        memo = {}
        def calculate(i, j):
            if i == m or j == n:
                return float('inf')

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = grid[i][j] + min(calculate(i + 1, j), calculate(i, j + 1))
            return memo[(i, j)]

        return calculate(0, 0)
