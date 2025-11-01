class Solution:
    '''
    coins = [1,2,5], amount = 5

    dp[i][0] = 1
    dp[i][s] = dp[i - 1][s]
    dp[i][s] += dp[i][s - coin]
    
      0 1 2 3 4 5
    0 1 0 0 0 0 0
    1 1 1 1 1 1 1
    2 1 1 2 2 3 3
    5 1 2 2 2 3 4

    '''
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for s in range(amount + 1):
                dp[i][s] = dp[i - 1][s]
                if s >= coins[i - 1]:
                    dp[i][s] += dp[i][s - coins[i - 1]]
        return dp[n][amount]
        