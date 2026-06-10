class Solution:
    def numWays(self, n: int, k: int) -> int:
        # RR, GG, RG, GR
        # RRG, GGR, GRG, RGR, GRR, GGR 
        # (2-1) * (2 + 4) = 1 * 6 = 6

        memo = {}

        def dp(i):
            if i == 1:
                return k

            if i == 2:
                return k * k

            if i in memo:
                return memo[i]

            memo[i] = (k - 1) * (dp(i - 1) + dp(i - 2))
            return memo[i]

        return dp(n)
       
