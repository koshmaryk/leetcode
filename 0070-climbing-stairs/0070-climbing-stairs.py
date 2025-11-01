class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def count(i):
            if i > n:
                return 0

            if i == n:
                return 1

            if i in memo:
                return memo[i]

            memo[i] = count(i + 1) + count(i + 2)
            return memo[i]

        return count(0)
                