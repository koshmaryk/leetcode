class Solution:
    '''
    [[0,30],[5,10],[15,20]]

    [(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)]

    2  1 2 1 0
    1+1-1+1-1-1

    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for s,e in intervals:
            events.append((s, 1))
            events.append((e, -1))

        events.sort()
        ans = curr = 0
        for _, weight in events:
            curr += weight
            ans = max(ans, curr)
        return ans
