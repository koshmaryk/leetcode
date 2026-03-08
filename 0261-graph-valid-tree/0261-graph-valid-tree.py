from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = {0: 0}
        queue = deque([0])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v == parent[u]:
                    continue

                if v in parent:
                    return False

                parent[v] = u
                queue.append(v)
        return len(parent) == n
