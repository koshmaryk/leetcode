from sortedcontainers import SortedList

"""

[1,7]

[5,6]

"""
class CountIntervals:

    def __init__(self):
        self.intervals = SortedList()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        i = self.intervals.bisect_left((left, -1))
        if i > 0 and self.intervals[i - 1][1] >= left:
            i -= 1

        while i < len(self.intervals) and self.intervals[i][0] <= right:
            l, r = self.intervals[i]
            left = min(left, l)
            right = max(right, r)
            self.cnt -= r - l + 1
            del self.intervals[i]

        self.intervals.add((left, right))
        self.cnt += right - left + 1
       

    def count(self) -> int:
        return self.cnt