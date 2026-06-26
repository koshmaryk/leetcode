"""
k = 2
n = 4

0 1 - 4
1 2 - 3
0 2 - 1
2 3 - 2 !!!

    0
  /   \
1  ___  2 ___ 3

edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0],[2,3,2,1]],

"""
from math import inf

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
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = -1

        if len(edges) < n - 1:
            return ans
            

        uf = UnionFind(n)
        
        cnt = 0
        must_s = inf
        opt = []
        for u,v,s,must in edges:
            if must == 1:
                if uf.find(u) == uf.find(v):
                    return -1

                uf.union(u, v)
                cnt += 1
                must_s = min(must_s, s)
            else:
                opt.append((u,v,s))

        opt.sort(key=lambda x: x[2], reverse=True)

        opt_s = inf
        upgraded = inf
        for i,(u,v,s) in enumerate(opt):
            if uf.find(u) == uf.find(v):
                continue

            uf.union(u, v)    
            cnt += 1

            if cnt == n - 1 - k:
                opt_s = s
            upgraded = s

        if cnt != n - 1:
            return -1
        return min(must_s, opt_s, upgraded * 2)
