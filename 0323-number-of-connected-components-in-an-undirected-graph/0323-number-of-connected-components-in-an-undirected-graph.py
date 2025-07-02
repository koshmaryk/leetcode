from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(u):
            queue = deque([u])
            while queue:
                u = queue.popleft()
                visited[u] = True

                for v in graph[u]:
                    if not visited[v]:
                        queue.append(v)

        visited = [False] * n

        count = 0
        for u in range(n):
            if not visited[u]:
                count += 1
                bfs(u)
        return count