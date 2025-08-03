class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n < 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = f(n - 1) + f(n - 2)
            return memo[n]

        memo = {}
        return f(n)
