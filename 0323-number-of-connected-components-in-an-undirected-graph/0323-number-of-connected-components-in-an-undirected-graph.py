from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)
        if self.size[x_root] > self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        uf = UnionFind(n)

        count = n
        for u in range(n):
            for v in graph[u]:
                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    count -= 1
        return count
        