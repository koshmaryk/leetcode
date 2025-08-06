class Solution:
    '''
    coins = [1,2,3], amount = 5

        0  1  2  3  4  5
    0   1  0  0  0  0  0
    1   1  1  1  1  1  1
    2   1  1  2  2  3  3
    3   1  1  2  3  4  5
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n):
            for curr in range(coins[i], amount + 1):
                dp[curr] += dp[curr - coins[i]]
        return dp[amount]
