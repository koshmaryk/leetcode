from collections import defaultdict
import heapq

class UnionFind:

    def __init__(self, c):
        self.parent = list(range(c))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root, v_root = self.find(u), self.find(v)
        if u_root != v_root:
            if u_root > v_root:
                self.parent[u_root] = v_root
            else:
                self.parent[v_root] = u_root

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c + 1)
        for u,v in connections:
            uf.union(u, v)

        answer = []

        online = set()
        groups = {}
        heaps = defaultdict(list)

        for u in range(c + 1):
            group_id = uf.find(u)
            groups[u] = group_id
            heapq.heappush(heaps[group_id], u)
            online.add(u)

        for y,x in queries:
            if y == 1:
                if x in online:
                    answer.append(x)
                else:
                    group = heaps[uf.find(x)]
                    while group and group[0] not in online:
                        heapq.heappop(group)

                    if group:
                        answer.append(group[0])
                    else:
                        answer.append(-1)
            else:
                online.discard(x)

        return answer