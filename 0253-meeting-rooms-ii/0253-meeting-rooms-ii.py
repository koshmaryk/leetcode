import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pq = []
        for s,e in intervals:
            if pq and pq[0] <= s:
                heapq.heappop(pq)

            heapq.heappush(pq, e)

        return len(pq)
