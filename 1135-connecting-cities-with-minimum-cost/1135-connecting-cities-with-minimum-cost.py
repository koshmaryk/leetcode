from collections import defaultdict
import heapq 

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y,cost in connections:
            graph[x].append((y, cost))
            graph[y].append((x, cost))

        in_mst = [False] * (n + 1)
        pq = [(0, 1)] # weight, ->node

        min_cost = cnt = 0
        while pq:
            cost, city = heapq.heappop(pq)

            if in_mst[city]:
                continue

            min_cost += cost
            in_mst[city] = True
            cnt += 1

            if cnt == n:
                return min_cost

            for next_city, next_cost in graph[city]:
                if not in_mst[next_city]:
                    heapq.heappush(pq, (next_cost, next_city))
        
        return -1
        