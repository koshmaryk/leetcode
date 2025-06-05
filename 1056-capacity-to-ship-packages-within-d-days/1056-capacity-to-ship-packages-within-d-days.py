class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isGoodEnough(max_weight):
            days_used = 0
            total = 0
            for weight in weights:
                if weight > max_weight:
                    return False

                if total + weight > max_weight:
                    days_used += 1
                    total = weight
                else:
                    total += weight
            return days_used + 1 <= days

        total = 0
        for weight in weights:
            total += weight

        bad = 0
        good = total + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
