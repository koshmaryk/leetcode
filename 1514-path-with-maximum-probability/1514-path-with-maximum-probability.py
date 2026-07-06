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

        pq = [(-1.0, start_node)]
        while pq:
            prob, node = heapq.heappop(pq)
            if node == end_node:
                return -prob

            for next_prob, next_node in graph[node]:
                new_prob = next_prob * -prob
                if new_prob > max_prob[next_node]:
                    max_prob[next_node] = new_prob
                    heapq.heappush(pq, (-new_prob, next_node))
        return 0.0

        