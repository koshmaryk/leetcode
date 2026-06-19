from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def bipartite(node, color):
            queue = deque([node])
            colors[node] = color
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if colors[v] == 0:
                        colors[v] = -colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False
            return True


        for node in range(n):
            if colors[node] == 0:
                if not bipartite(node, 1):
                    return False
        return True
