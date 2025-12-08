import heapq

'''
    [[10, 20], [20, 30], [40, 50]]

    [60, 75]
'''
class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for start,end in self.calendar:
            if startTime < end and endTime > start:
                return False
        self.calendar.append((startTime, endTime))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)