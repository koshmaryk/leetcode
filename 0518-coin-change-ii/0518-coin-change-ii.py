class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        print(dp)

        for i in range(1, n + 1):
            for curr in range(1, amount + 1):
                dp[i][curr] = dp[i - 1][curr]
                if coins[i - 1] <= curr:
                     dp[i][curr] += dp[i][curr - coins[i - 1]]
        return dp[n][amount]
