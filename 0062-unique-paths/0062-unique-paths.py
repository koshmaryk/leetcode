class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == 0 or j == 0:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = dfs(i, j - 1) + dfs(i - 1, j)
            return memo[(i, j)]

        memo = {}
        return dfs(m - 1, n - 1)