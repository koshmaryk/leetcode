class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1

        k = 2
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i] += dp[i - j]
        return dp[n]
        