from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n # 0,1

        def bipartite(u, color):
            if colors[u] != -1:
                return colors[u] == color

            colors[u] = color
            for v in graph[u]:
                if not bipartite(v, 1 - color):
                    return False
            return True


        for node in range(n):
            if colors[node] == -1:
                if not bipartite(node, 1):
                    return False
        return True
