class Solution:
    def mySqrt(self, x: int) -> int:
        bad = 0
        good = x
        while good - bad > 0.00001:
            mid = (bad + good) / 2
            if mid * mid >= x:
                good = mid
            else:
                bad = mid
        return int(good)

        