"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

1,2; 5,6
1,3
4,10


"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        for s in schedule:
            for interval in s:
                events.append((interval.start, 1))
                events.append((interval.end, -1))

        events.sort(key=lambda e: (e[0], -e[1]))

        output = []

        prev = float('-inf')
        balance = 0
        for timestamp, event_type in events:
            if balance == 0 and prev != float('-inf'):
                output.append(Interval(prev, timestamp))

            balance += event_type
            prev = timestamp
        return output
