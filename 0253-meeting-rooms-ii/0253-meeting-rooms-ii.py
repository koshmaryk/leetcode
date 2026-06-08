"""

0,10; 10,20; 20,30 -> 1
0,10; 5,20; 0,30 -> 3
0,10; 5,20; 10,30 -> 2

1. sort by start
2. pop if earliest end less then curr start
3. add to



"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for s,e in intervals:
            events.append((s, 1))
            events.append((e, -1))

        events.sort()

        ans = curr = 0
        for _,weight in events:
            curr += weight
            ans = max(ans, curr)
        return ans
        