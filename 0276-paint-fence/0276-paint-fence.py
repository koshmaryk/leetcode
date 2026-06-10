class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        if n == 2:
            return k * k
       
        a, b = k, k*k # RR, GG, RG, GR
        # RRG, GGR, GRG, RGR, GRR, GGR 
        # (2-1) * (2 + 4) = 1 * 6 = 6
        for i in range(2, n):
            a, b = b, (k - 1) * (a + b)
        return b
