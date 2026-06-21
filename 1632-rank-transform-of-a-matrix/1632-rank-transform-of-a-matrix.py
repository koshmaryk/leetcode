from collections import defaultdict

class UnionFind:
    def __init__(self, m, n):
        self.parent = list(range(m + n))
        self.rank = [0] * (m + n) # row r = rank[r], col c = rank[m + c]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        cells = defaultdict(list)
        for r in range(m):
            for c in range(n):
                cells[matrix[r][c]].append((r, c))

        row_rank = [0] * m
        col_rank = [0] * n
        answer = [[0] * n for _ in range(m)]
        for v in sorted(cells):
            uf = UnionFind(m, n)

            for r,c in cells[v]:
                uf.union(r, m + c)

            rank = {}
            for r,c in cells[v]:
                root = uf.find(r)
                rank[root] = max(
                    rank.get(root, 0),
                    row_rank[r],
                    col_rank[c]
                )

            for r,c in cells[v]:
                root = uf.find(r)
                answer[r][c] = rank[root] + 1
                row_rank[r] = max(row_rank[r], rank[root] + 1)
                col_rank[c] = max(col_rank[c], rank[root] + 1)
            
        return answer   
        