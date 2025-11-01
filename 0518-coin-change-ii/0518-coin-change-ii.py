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
        memo = {}
        
        def f(i, s):
            if s == 0:
                return 1

            if i == n or s < 0:
                return 0

            if (i, s) in memo:
                return memo[(i, s)]

            memo[(i, s)] = f(i + 1, s) + f(i, s - coins[i])
            return memo[(i, s)]

        return f(0, amount)
        