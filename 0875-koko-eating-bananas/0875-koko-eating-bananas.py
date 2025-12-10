class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total


        bad, good = 0, max(piles) + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if eat(guess) <= h:
                good = guess
            else:
                bad = guess
        return good