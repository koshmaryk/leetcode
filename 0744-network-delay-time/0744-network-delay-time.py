from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = []
        heapq.heappush(pq, (0, k))

        visited = set()
        while pq:
            curr_time, u = heapq.heappop(pq)
            visited.add(u)

            if len(visited) == n:
                return curr_time
            
            for v, travel_time in graph.get(u, []):
                if v not in visited:
                    heapq.heappush(pq, (curr_time + travel_time, v))
        return -1