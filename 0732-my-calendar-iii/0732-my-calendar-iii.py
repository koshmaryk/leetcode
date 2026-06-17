from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> int:
        self.diff[startTime] = self.diff.get(startTime, 0) + 1
        self.diff[endTime] = self.diff.get(endTime, 0) - 1
        
        max_overlaps = 0
        overlaps = 0
        for count in self.diff.values():
            overlaps += count
            max_overlaps = max(max_overlaps, overlaps)

        return max_overlaps
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)