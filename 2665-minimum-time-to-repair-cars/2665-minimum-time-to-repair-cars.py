class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isGoodEnough(t):
            repaired = 0
            for rank in ranks:
                repaired += int((t / rank) ** 0.5)
            return repaired >= cars

        bad, good = 0, 101 * cars ** 2
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good

