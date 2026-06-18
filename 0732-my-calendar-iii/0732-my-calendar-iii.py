"""

        0,7

   0,3     4,7

0,1  2,3    4,5  6,7

0 1  2 3    4 5  6 7

1   [0,7] 3,0
2   [0,3] 3,1
3   [4,7] 3,0
4   [0,1] 
5   [2,3] 2,1
6   [4,5] 3,1
7   [6,7] 1,1
8   [0,0]
9   [1,1]
10  [2,2]
11  [3,3] 1,1
12  [4,4] 2,2
13  [5,5]
14  [6,6]
15  [7,7]


[2,6)
[0,5)
[6,8)
[3,5)

"""
from collections import Counter

# class MyCounter(Counter):
#     def __str__(self):
#         return ", ".join('{} {}'.format(k, v) for k, v in sorted(self.items()))

class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()
        
    def update(self, startTime, endTime, left = 0, right = 10**9, idx = 1):
        # case 1: completely outside
        if startTime > right or endTime < left:
            return

        # case 1: completely inside
        if startTime <= left and right <= endTime:
            self.vals[idx] += 1
            self.lazy[idx] += 1 # differ children update
        else: # case 3: partially inside
            mid = (left + right) // 2
            self.update(startTime, endTime, left, mid, idx * 2)
            self.update(startTime, endTime, mid + 1, right, idx * 2 + 1)
            self.vals[idx] = self.lazy[idx] + max(self.vals[idx * 2], self.vals[idx * 2 + 1])

    def book(self, startTime: int, endTime: int) -> int:
        self.update(startTime, endTime - 1)
        # print("vals: " + str(self.vals))
        # print("lazy: " + str(self.lazy))
        return self.vals[1]
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)