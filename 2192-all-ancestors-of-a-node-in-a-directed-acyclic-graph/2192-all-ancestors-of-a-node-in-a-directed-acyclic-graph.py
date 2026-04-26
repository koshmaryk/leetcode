from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for f,t in edges:
            graph[t].append(f)

        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)

        answer = []
        for u in range(n):
            visited = set()
            dfs(u)

            ancestors = []
            for node in range(n):
                if node in visited and node != u:
                    ancestors.append(node)

            answer.append(ancestors)

        return answer
            