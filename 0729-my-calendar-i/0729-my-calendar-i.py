import heapq

'''
[[10,20], [30,40], [40,50]]

[55,65]

'''
class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.calendar:
            # e1 <= s2 or e2 <= s1
            if e > startTime and endTime > s:
                return False
        self.calendar.append((startTime, endTime))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)