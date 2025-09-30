class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def f(x, m):
            if m == 0:
                return 1

            if m < 0:
                m = -m
                x = 1.0 / x

            result = 1
            while m != 0:
                if m % 2 == 1:
                    result = result * x % mod
                    m -= 1

                x = x * x % mod
                m //= 2
            return result


        odd = (n + 1) // 2
        even = n // 2
        return (f(4, even) * f(5, odd)) % mod
        