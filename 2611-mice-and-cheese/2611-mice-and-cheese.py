"""
10

7


10
+
7
=
17
-
1
1
=15

n + n log k


2
3


"""
import heapq

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        points = sum(reward2) # 8

        if k == 0:
            return points
        
        pq = []
        for i in range(n):
            gain = reward1[i] - reward2[i]
            if len(pq) < k:
                heapq.heappush(pq, gain)
            elif gain > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, gain)
        points += sum(pq)
        return points
