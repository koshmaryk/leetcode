"""
1 1 1 1 1
1 2 3 4 5
1 3 6 10 15


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
