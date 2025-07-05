from collections import defaultdict

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        in_degree = defaultdict(list)
        candidate_1 = candidate_2 = []
        for u,v in edges:
            in_degree[v].append(u)
            if len(in_degree[v]) == 2:
                candidate_1 = [in_degree[v][0], v]
                candidate_2 = [in_degree[v][1], v]
                break


        def detectCycle(skip_edge: List[int]):
            uf = UnionFind(len(edges) + 1)
            for edge in edges:
                if edge == skip_edge:
                    continue
                if not uf.union(edge[0], edge[1]):
                    return edge
            return []
        
        
        if not candidate_1 and not candidate_2:
            return detectCycle([])
        
        if not detectCycle(candidate_2):
            return candidate_2
        else:
            return candidate_1
            
