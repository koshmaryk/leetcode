"""


0,30; 5,10; 15,20


"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort()
        for i in range(n - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True