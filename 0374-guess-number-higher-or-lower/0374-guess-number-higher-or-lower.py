# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bad = -1
        good = n + 1
        while good - bad > 1:
            mid = (bad + good) // 2
            if guess(mid) <= 0:
                good = mid
            else:
                bad = mid
        return good
        