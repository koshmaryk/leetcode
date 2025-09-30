class Solution:
    '''
    x^n

    brute-force:
    x * f(x, n - 1)

    optimized:

    even (x^2) ^ n/2
    odd x * (x^2) ^ (n-1)/2
    
    if n >= 0 -> f(x, n)
    if n < 0 -> 1.0 / f(x, -n)


    '''
    def myPow(self, x: float, n: int) -> float:
        def f(x, n):
            if n == 0:
                return 1

            if n < 0:
                return 1.0 / self.myPow(x, -n)

            if n % 2 == 0:
                return self.myPow(x * x, n // 2)
            else:
                return x * self.myPow(x * x, (n - 1) // 2)

        return f(x, n)
        