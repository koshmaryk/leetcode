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
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1.0 / x

        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n //= 2
        return result