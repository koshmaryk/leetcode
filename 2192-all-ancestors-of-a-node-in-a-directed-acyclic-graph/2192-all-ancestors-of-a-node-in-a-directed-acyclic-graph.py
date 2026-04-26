from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for f,t in edges:
            graph[f].append(t)

        answer = [[] for _ in range(n)]

        def dfs(u, ancestor):
            for v in graph[u]:
                if not answer[v] or answer[v][-1] != ancestor:
                    answer[v].append(ancestor)
                    dfs(v, ancestor)
        
        for u in range(n):
           dfs(u, u)

        return answer

            