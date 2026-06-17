"""
[10,20], [10,35], [30,40], [50,60]

[15,25]

10  15  20  25  30  35  40  50  60 
+2  0   -1  0   +1  -1  -1  +1  -1

s1,e1
s2,e2

e2 <= s1 or e1 <= s2
s1 < e2 and s2 < e1

"""
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
       self.diff = SortedDict()
       self.max_overlaps = 2
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.diff[startTime] = self.diff.get(startTime, 0) + 1
        self.diff[endTime] = self.diff.get(endTime, 0) - 1

        overlaps = 0
        for count in self.diff.values():
            overlaps += count
            if overlaps > self.max_overlaps:
                self.diff[startTime] -= 1
                if self.diff[startTime] == 0:
                    del self.diff[startTime]

                self.diff[endTime] += 1
                if self.diff[endTime] == 0:
                    del self.diff[endTime]

                return False
        
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)