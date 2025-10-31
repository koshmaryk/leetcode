class Solution:
    '''
    [1,3,1],
    [1,5,1],
    [4,2,1]

    [7,6,3],
    [8,7,2],
    [7,3,1]

    [7,6,3]

    dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])

    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #dp = [[0] * n for _ in range(m)]
        dp = [0 for _ in range(n)]
        for i in range(m - 1, - 1, -1):
            for j in range(n - 1, - 1, -1):
                if i == m - 1 and j != n - 1:
                    #dp[i][j] = grid[i][j] + dp[i][j + 1]
                    dp[j] = grid[i][j] + dp[j + 1]
                elif i != m - 1 and j == n - 1:
                    #dp[i][j] = grid[i][j] + dp[i + 1][j]
                    dp[j] = grid[i][j] + dp[j]
                elif i != m - 1 and j != n - 1:
                    #dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
                    dp[j] = grid[i][j] + min(dp[j + 1], dp[j])
                else:
                    #dp[i][j] = grid[i][j]
                    dp[j] = grid[i][j]
        #return dp[0][0]
        return dp[0]