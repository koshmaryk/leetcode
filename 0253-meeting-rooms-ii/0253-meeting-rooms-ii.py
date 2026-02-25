class Solution:
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
