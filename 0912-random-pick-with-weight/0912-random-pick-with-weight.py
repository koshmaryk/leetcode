import random

class Solution:
    '''
        [1,2,3]
        [1,2,2,3,3,3]

        [0,1,3,6]

        [0,1)
        [1,3)
        [3,6)

        0-5

    '''

    def __init__(self, weights: List[int]):
        n = len(weights)
        self.p = [0] * (n + 1)
        for i in range(n):
            self.p[i + 1] = self.p[i] + weights[i]

    def pickIndex(self) -> int:
        target = self.p[-1] * random.random()
        bad, good = -1, len(self.p)
        while good - bad > 1:
            mid = (bad + good) // 2
            if self.p[mid] > target:
                good = mid
            else:
                bad = mid
        return good - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()