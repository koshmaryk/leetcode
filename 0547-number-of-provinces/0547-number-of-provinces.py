from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(u):
            queue = deque([u])
            while queue:
                u = queue.popleft()
                visited[u] = True

                for v in range(len(isConnected)):
                    if isConnected[u][v] == 1 and not visited[v]:
                        queue.append(v)

        visited = [False] * len(isConnected)

        ccs = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                ccs += 1
                bfs(i)
        return ccs