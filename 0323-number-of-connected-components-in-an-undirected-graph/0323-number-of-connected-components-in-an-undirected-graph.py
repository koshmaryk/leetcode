from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)

        visited = [False] * n

        count = 0
        for u in range(n):
            if not visited[u]:
                count += 1
                dfs(u)
        return count