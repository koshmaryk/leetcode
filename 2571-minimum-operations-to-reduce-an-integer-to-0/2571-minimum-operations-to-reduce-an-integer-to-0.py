"""
n & 1 == 1

2^0 = 1

cnt += 1

even vs. odd


2^0=1

111=7

111
&
 10
=
 1

111 + 1 = 1000 = 8

====

101=5

101
&
 10
=
 0

101 - 1 = 100 = 4

"""
class Solution:
    def minOperations(self, n: int) -> int:
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
                n = n + 1 if (n & 2) else n - 1
            n >>= 1
        return cnt
