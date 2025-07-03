class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(u):
            for v in graph[u]:
                if v == parent[u]:
                    continue
                if v in parent:
                    return False
                parent[v] = u
                dfs(v)
            return True

        parent = {0: 0}
        if not dfs(0):
            return False
        return len(parent) == n
