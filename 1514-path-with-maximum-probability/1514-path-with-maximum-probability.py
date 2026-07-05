from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u,v) in enumerate(edges):
            graph[u].append((succProb[i], v))
            graph[v].append((succProb[i], u))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        for _ in range(n - 1):
            updated = False
            for i, (u,v) in enumerate(edges):
                if succProb[i] * max_prob[u] > max_prob[v]:
                    max_prob[v] = succProb[i] * max_prob[u]
                    updated = True

                if succProb[i] * max_prob[v] > max_prob[u]:
                    max_prob[u] = succProb[i] * max_prob[v]
                    updated = True

            if not updated:
                break

        return max_prob[end_node]
        