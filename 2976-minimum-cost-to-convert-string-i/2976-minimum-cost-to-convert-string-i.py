"""
TC O(n) # n * 2 * 26 * log 26
SC O(1) # 26^2

"""
from collections import defaultdict
import heapq
from math import inf


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)

        graph = [[] for _ in range(26)]
        for i in range(m):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            graph[u].append((v, cost[i]))

        def dijkstra(s):
            pq = [(0, s)]
            dist = [inf] * 26
            dist[s] = 0
            while pq:
                d, c = heapq.heappop(pq)

                for next_c, next_d in graph[c]:
                    new_d = next_d + d
                    if new_d < dist[next_c]:
                        dist[next_c] = new_d
                        heapq.heappush(pq, (new_d, next_c))
            return dist

        dist = [dijkstra(s) for s in range(26)]

        total_cost = 0
        for i in range(n):
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            if dist[s][t] == inf:
                return -1
            total_cost += dist[s][t]

        return total_cost
