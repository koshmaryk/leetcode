"""

        0,7

   0,3         4,7

0,1  2,3    4,5  6,7

0 1  2 3    4 5  6 7


"""
from collections import Counter

class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()
        
    def update(self, startTime, endTime, left = 0, right = 10**9, idx = 1):
        # case 1: completely outside
        if startTime > right or endTime < left:
            return

        # case 1: completely inside
        if startTime <= left <= right <= endTime:
            self.vals[idx] += 1
            self.lazy[idx] += 1 # deffer children update
        else: # case 3: partially inside
            mid = (left + right) // 2
            self.update(startTime, endTime, left, mid, idx * 2)
            self.update(startTime, endTime, mid + 1, right, idx * 2 + 1)
            self.vals[idx] = self.lazy[idx] + max(self.vals[idx * 2], self.vals[idx * 2 + 1])

    def book(self, startTime: int, endTime: int) -> int:
        self.update(startTime, endTime - 1)
        return self.vals[1]
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)