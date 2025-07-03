class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parent = {0: 0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v == parent[u]:
                    continue
                if v in parent:
                    return False
                parent[v] = u
                stack.append(v)

        return len(parent) == n
