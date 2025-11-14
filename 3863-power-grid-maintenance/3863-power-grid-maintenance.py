from collections import defaultdict
import heapq


# TC O(c log c + M)
# SC O(c)
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        answer = []

        online = set() # O(c)
        groups = {} # O(c)
        heaps = defaultdict(list) # O(c)

        def dfs(u, idx):
            if u in online:
                return

            groups[u] = idx # O(1)
            heapq.heappush(heaps[idx], u) # O(log c)
            online.add(u) # O(1)

            for v in graph[u]:
                dfs(v, idx)

        # O(c log c)
        idx = 0
        for u in range(1, c + 1):
            dfs(u, idx)
            idx += 1

        # TC O(c log c)
        for y,x in queries:
            if y == 1:
                if x in online: # O(1)
                    answer.append(x)
                else:
                    group = heaps[groups[x]] # O(1)
                    while group and group[0] not in online:
                        heapq.heappop(group) # O(log c)

                    if group:
                        answer.append(group[0])
                    else:
                        answer.append(-1)
            else:
                online.discard(x) # O(1)

        return answer