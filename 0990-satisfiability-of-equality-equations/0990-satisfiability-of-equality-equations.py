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
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[rx] = ry
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        def extract_components(eq):
            op = eq[1] + eq[2]
            var1 = ord(eq[0]) - ord('a')
            var2 = ord(eq[3]) - ord('a')
            return var1, op, var2

        for eq in equations:
            var1, op, var2 = extract_components(eq)
            if op == "==":
                uf.union(var1, var2)

        for eq in equations:
            var1, op, var2 = extract_components(eq)
            if op == "!=":
                if uf.find(var1) == uf.find(var2):
                    return False
        return True
            