import math

class Solution:
    '''
    n = 6, quantities = [11,6]

    1,2 = 3
    3,4,5 = 3
    6 = 2

    '''
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)

        def isGoodEnough(x):
            return sum([math.ceil(quantity / x) for quantity in quantities]) <= n

        bad, good = 0, max(quantities)
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
