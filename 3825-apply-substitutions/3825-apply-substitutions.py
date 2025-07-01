from collections import defaultdict
import heapq

class Solution:
    # A, B -> C 
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        lookup = {key:val for key,val in replacements} # N

        graph = defaultdict(set) # N
        in_degree = defaultdict(int) # N
        for key,val in replacements:
            for other_key,_ in replacements: # N^2
                if f"%{other_key}%" in val: # MaxStringLength * MaxKeyLength
                    graph[other_key].add(key)
                    in_degree[key] += 1

        queue = deque([u for u in lookup if in_degree[u] == 0]) # N

        toposort = []
        # N + D
        while queue:
            u = queue.popleft()
            toposort.append(u)

            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        #  0  1  2
        # [A, B, C]
        for i in range(len(toposort)):
            key, val = toposort[i], lookup[toposort[i]]
            for j in range(i): # N^2
                prev_key, prev_val = toposort[j], lookup[toposort[j]]
                if key in graph[prev_key]:
                    val = val.replace(f"%{prev_key}%", prev_val) # MaxStringLength * MaxKeyLength
            lookup[key] = val
            text = text.replace(f"%{key}%", val) # MaxStringLength * MaxKeyLength
        return text