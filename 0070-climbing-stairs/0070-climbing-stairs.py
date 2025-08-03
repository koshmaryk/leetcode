class Solution:
    def climbStairs(self, n: int) -> int:
        def count(n):
            if n < 2:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = count(n - 1) + count(n - 2)
            return memo[n]

        memo = {}
        return count(n)