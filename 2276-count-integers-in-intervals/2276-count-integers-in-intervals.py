from collections import Counter

class CountIntervals:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()

    def update(self, left, right, start=0, end=10**9, idx=1):
        if self.lazy[idx]:
            return

        if left > end or right < start:
            return

        if left <= start and right >= end:
            self.vals[idx] = end - start + 1
            self.lazy[idx] = True
        else:
            mid = (start + end) // 2
            self.update(left, right, start, mid, 2*idx)
            self.update(left, right, mid + 1, end, 2*idx + 1)
            self.vals[idx] = self.vals[2*idx] + self.vals[2*idx + 1]

    def add(self, left: int, right: int) -> None:
        self.update(left, right)
        

    def count(self) -> int:
        return self.vals[1]
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()