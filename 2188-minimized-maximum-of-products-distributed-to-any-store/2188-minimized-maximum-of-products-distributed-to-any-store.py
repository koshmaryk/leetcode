class Solution:
    '''
    n = 6, quantities = [11,6]

    1,2 = 3
    3,4,5 = 3
    6 = 2

    '''
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        maximum = max(quantities)

        def isGoodEnough(x):
            i = 0
            quantity = quantities[i]
            for _ in range(n):
                if quantity <= x:
                    i += 1
                    if i == m:
                        return True
                    else:
                       quantity = quantities[i]
                else:
                    quantity -= x
            return False

        bad, good = 0, maximum
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
