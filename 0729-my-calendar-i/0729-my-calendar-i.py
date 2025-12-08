import heapq

'''
    [[10, 20], [20, 30], [40, 50]]

    [10, 20] and [60, 75]
    [s1, e1] and [s2, e2]

    e1 <= s2 or e2 <= s1
    e1 > s2 and e2 > s1

'''
class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for start,end in self.calendar:
            if endTime > start and startTime < end:
                return False
        self.calendar.append((startTime, endTime))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)