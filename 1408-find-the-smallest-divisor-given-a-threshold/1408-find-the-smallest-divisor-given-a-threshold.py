class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isGoodEnough(divisor):
            s = 0
            for num in nums:
                s += (num + divisor - 1) // divisor
            return s <= threshold

        bad, good = 0, sum(nums)
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
        