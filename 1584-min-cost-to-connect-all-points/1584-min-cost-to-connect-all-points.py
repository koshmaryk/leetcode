class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] < self.rank[ry]:
            self.rank[rx] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for u in range(n):
            for v in range(u + 1, n):
                weight = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                edges.append((weight, u, v))
        
        edges.sort()

        uf = UnionFind(n)
        cost = cnt = 0
        for weight, u, v in edges:
            if uf.union(u, v):
                cost += weight
                cnt += 1

                if cnt == n - 1:
                    break
            
        return cost

        