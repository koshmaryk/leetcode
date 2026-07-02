import heapq
from math import inf


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)

        def distance(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        
        def count_ones(mask):
            cnt = 0
            while mask:
                mask &= (mask - 1)
                cnt += 1
            return cnt


        dist = [inf] * (1 << m)
        dist[0] = 0

        pq = [(0, 0)] # cost, mask
        while pq:
            cost, mask = heapq.heappop(pq)
            i = count_ones(mask)
            if i == n:
                return cost

            for j in range(m):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    new_cost = cost + distance(i, j)
                    if new_cost < dist[new_mask]:
                        dist[new_mask] = new_cost
                        heapq.heappush(pq, (new_cost, new_mask))
        return -1
         