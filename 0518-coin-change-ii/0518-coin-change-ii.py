class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def f(i, curr):
            if curr == 0:
                return 1

            if i == len(coins) or curr < 0:
                return 0

            if (i, curr) in memo:
                return memo[(i, curr)]
            
            memo[(i, curr)] = f(i, curr - coins[i]) + f(i + 1, curr)
            return memo[(i, curr)]

        memo = {}
        return f(0, amount)