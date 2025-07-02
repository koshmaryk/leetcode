from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v, w))

        visited = set()
        pq = [(0, k)]
        while pq:
            curr_time, u = heapq.heappop(pq)
            visited.add(u)

            if len(visited) == n:
                return curr_time

            for v, next_time in graph[u]:
                if v not in visited:
                    heapq.heappush(pq, (curr_time + next_time, v))
        return -1
