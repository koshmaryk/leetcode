from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        def bipartite(node):
            queue = deque([(node, 1)])
            while queue:
                u, color = queue.popleft()

                if u in colors:
                    if colors[u] != color:
                        return False
                    continue

                colors[u] = color
                for v in graph[u]:
                    queue.append((v, -color))

            return True

        for u in range(len(graph)):
            if u not in colors:
                if not bipartite(u):
                    return False
        return True