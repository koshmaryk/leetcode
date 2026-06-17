"""


s1,e1
s2,e2

e2 <= s1 or e1 <= s2
s1 < e2 and s2 < e1

"""
class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        self.overlaps = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.overlaps:
            if startTime < e and s < endTime:
                return False

        for s,e in self.intervals:
            if startTime < e and s < endTime:
                self.overlaps.append((max(startTime, s), min(endTime, e)))

        self.intervals.append((startTime, endTime))
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)