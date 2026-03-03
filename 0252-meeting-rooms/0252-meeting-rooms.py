"""


0,30; 5,10; 15,20


"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] <= interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return len(merged) == len(intervals)