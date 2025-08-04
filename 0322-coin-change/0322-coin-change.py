class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def f(amount):
            if amount < 0:
                return float('inf')

            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            count = float('inf')
            for coin in coins:
                count = min(count, 1 + f(amount - coin))
            memo[amount] = count
            return memo[amount]

        memo = {}
        ans = f(amount)
        return -1 if ans == float('inf') else ans