import math

class Solution:
    # 3,6,7,11
    # 3/4 = 1h, 6/4 = 2h, 7/4 = 2h, 11/4 = 3h -> 1+2+2+3 = 8h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isGoodEnough(min_k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / min_k)
            return total <= h

        bad = 0
        good = 1
        for pile in piles:
            good += pile

        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good

    # bad = 3, good = 5
    # 14 -> 3/14 = 1h, 6/14 = 1h, 7/14 = 1h, 11/14 = 1h -> 1+1+1+1 = 4h
    # 7 -> 3/7 = 1h, 6/7 = 1h, 7/7 = 1h, 11/7 = 2h -> 1+1+1+2 = 5h
    # 3 -> 3/3 = 1h, 6/3 = 2h, 7/3 = 3h, 11/3 = 4h -> 1+2+3+4 = 10h
    # 5 -> 3/5 = 1h, 6/5 = 2h, 7/5 = 2h, 11/5 = 3h -> 1+2+2+3 = 8h
    # 4 -> 3/4 = 1h, 6/4 = 2h, 7/4 = 2h, 11/4 = 3h -> 1+2+2+3 = 8h