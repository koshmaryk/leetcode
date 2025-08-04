class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for curr in range(1, amount + 1):
            for coin in coins:
                if curr >= coin:
                    dp[curr] = min(dp[curr], 1 + dp[curr - coin])
        return -1 if dp[amount] == float('inf') else dp[amount]