from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def bipartite(u, color):
            if colors[u] != 0:
                return colors[u] == color

            colors[u] = color
            for v in graph[u]:
                if not bipartite(v, -color):
                    return False
            return True


        for node in range(n):
            if colors[node] == 0:
                if not bipartite(node, 1):
                    return False
        return True
