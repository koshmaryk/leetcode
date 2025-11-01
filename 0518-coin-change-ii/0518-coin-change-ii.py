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
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for s in range(coin, amount + 1):
                dp[s] += dp[s - coin]
        return dp[amount]
        