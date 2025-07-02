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
        uf = UnionFind(n)
        count = n
        for a,b in edges:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                count -= 1
        return count
        