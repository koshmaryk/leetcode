class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isGoodEnough(capacity):
            days_needed = 1
            total = 0
            for weight in weights:
                if weight > capacity:
                    return False
                if total + weight <= capacity:
                    total += weight
                else:
                    days_needed += 1
                    total = weight
            return days_needed <= days

        bad, good = 0, sum(weights)
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
