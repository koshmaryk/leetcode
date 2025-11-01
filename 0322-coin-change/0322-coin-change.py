class Solution:
    ''' 
    dp[s] = min(dp[s], 1 + dp[s - coin])
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for s in range(amount + 1):
            for coin in coins:
                if s >= coin:
                    dp[s] = min(dp[s], 1 + dp[s - coin])
        return -1 if dp[amount] == float('inf') else dp[amount]
        