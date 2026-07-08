from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v, t))

        visited = set()
        pq = [(0, k)]
        while pq:
            time, node = heapq.heappop(pq)
            
            visited.add(node)
            if len(visited) == n:
                return time

            for next_node, next_time in graph[node]:
                if next_node not in visited:
                    heapq.heappush(pq, (time + next_time, next_node))
        return -1
                