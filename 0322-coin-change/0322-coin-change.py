class Solution:
    ''' 
    dp[s] = min(dp[s], 1 + dp[s - coin])
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def f(s):
            if s < 0:
                return float('inf')
            
            if s == 0:
                return 0

            if s in memo:
                return memo[s]

            count = float('inf')
            for coin in coins:
                count = min(count, 1 + f(s - coin))
            memo[s] = count
            return memo[s]


        ans = f(amount)
        return -1 if ans == float('inf') else ans
        