"""
    1
3       2

[1,2], [1,3], [2,3]


0,1,1,1
1,3,1,1

[1,2] -> 1 vs 2
[1,3] -> 1 vs 3
[2,3] -> 1 vs 1

"""
class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return False

        if self.rank[parent_a] >= self.rank[parent_b]:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += self.rank[parent_a]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        for a,b in edges:
            if not uf.union(a, b):
                return [a, b]
        return [-1, -1]