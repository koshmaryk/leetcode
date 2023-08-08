class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        def count(n: int) -> int:
            if n == 0 or n == 1:
                return 1

            if memo[n] > 0:
                return memo[n]

            memo[n] = count(n - 1) + count(n - 2)
            return memo[n]

        return count(n)
        