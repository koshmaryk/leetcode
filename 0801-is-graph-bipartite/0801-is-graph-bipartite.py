class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        def bipartite(u, color):
            if u in colors:
                return colors[u] == color

            colors[u] = color
            for v in graph[u]:
                if not bipartite(v, -color):
                    return False
            return True

        for u in range(len(graph)):
            if u not in colors:
                if not bipartite(u, 1):
                    return False
        return True