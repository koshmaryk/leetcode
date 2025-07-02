class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(u):
            visited[u] = True
            for v in range(len(isConnected)):
                if isConnected[u][v] and not visited[v]:
                    dfs(v)

        visited = [False] * len(isConnected)

        count = 0
        for u in range(len(isConnected)):
            if not visited[u]:
                count += 1
                dfs(u)
        return count