from collections import defaultdict
import heapq

class Solution:
    # A, B -> C 
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        lookup = {key:val for key,val in replacements}
        
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        for key,val in replacements:
            for other_key,_ in replacements:
                if f"%{other_key}%" in val:
                    graph[other_key].add(key)
                    in_degree[key] += 1

        pq = [u for u in lookup if in_degree[u] == 0]
        heapq.heapify(pq)

        toposort = []
        while pq:
            u = heapq.heappop(pq)
            toposort.append(u)

            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    heapq.heappush(pq, v)
        
        #  0  1  2
        # [A, B, C]
        for i in range(len(toposort)):
            key, val = toposort[i], lookup[toposort[i]]
            for j in range(i):
                prev_key, prev_val = toposort[j], lookup[toposort[j]]
                if key in graph[prev_key]:
                    val = val.replace(f"%{prev_key}%", prev_val)
            lookup[key] = val
            text = text.replace(f"%{key}%", val)
        return text