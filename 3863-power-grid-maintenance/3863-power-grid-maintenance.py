from collections import defaultdict
import heapq

# TC O(M * Ⲁ(c)), where M = len(connections)
# SC O(c)
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

# TC O(c log c + M)
# SC O(c)
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c + 1)
        for u,v in connections:
            uf.union(u, v)

        answer = []

        online = set() # O(c)
        groups = {} # O(c)
        heaps = defaultdict(list) # O(c)

        # O(c log c)
        for u in range(c + 1):
            group_id = uf.find(u) # Ⲁ(c)
            groups[u] = group_id # O(1)
            heapq.heappush(heaps[group_id], u) # O(log c)
            online.add(u) # O(1)

        # TC O(c log c)
        for y,x in queries:
            if y == 1:
                if x in online: # O(1)
                    answer.append(x)
                else:
                    group = heaps[uf.find(x)] # O(Ⲁ(n))
                    while group and group[0] not in online:
                        heapq.heappop(group) # O(log c)

                    if group:
                        answer.append(group[0])
                    else:
                        answer.append(-1)
            else:
                online.discard(x) # O(1)

        return answer