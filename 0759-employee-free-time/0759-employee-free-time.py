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
import heapq

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        pq = []
        for idx, employee in enumerate(schedule):
            interval = employee[0]
            pq.append((interval.start, interval.end, idx, 0))
        heapq.heapify(pq)

        output = []

        prev_end = pq[0][1]
        while pq:
            start, end, employee_idx, interval_idx = heapq.heappop(pq)

            if prev_end < start:
                output.append(Interval(prev_end, start))

            prev_end = max(prev_end, end)

            if interval_idx + 1 < len(schedule[employee_idx]):
                next_interval = schedule[employee_idx][interval_idx + 1] 
                heapq.heappush(pq, (next_interval.start, next_interval.end, employee_idx, interval_idx + 1))
        return output


