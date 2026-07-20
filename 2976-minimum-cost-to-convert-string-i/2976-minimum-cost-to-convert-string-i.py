"""
TC O((26 + m) log 26 + n) # O((26 + m) log 26 * n)
SC O(26^2 + (26 + m))

"""
from collections import defaultdict
import heapq
from math import inf


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)

        dist = [[inf] * 26 for _ in range(26)]
        for s in range(26):
            dist[s][s] = 0

        for i in range(m):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for i in range(n):
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            if dist[s][t] == inf:
                return -1
            total_cost += dist[s][t]
        return total_cost
