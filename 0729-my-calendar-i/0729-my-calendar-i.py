import heapq

'''
[[10,20], [30,40], [45,50]]

[40,45]

'''
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()
        

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.calendar.bisect_right((startTime, endTime))
        if (idx > 0 and self.calendar[idx - 1][1] > startTime) or (idx < len(self.calendar) and self.calendar[idx][0] < endTime):
            return False
        self.calendar.add((startTime, endTime))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)