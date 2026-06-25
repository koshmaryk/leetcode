from collections import defaultdict
import heapq

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, cost in enumerate(wells):
            graph[0].append((i + 1, cost))
            graph[i + 1].append((0, cost))

        for x,y, cost in pipes:
            graph[x].append((y, cost))
            graph[y].append((x, cost))

        min_cost = cnt = 0
        in_mst = [False] * (n + 1)
        pq = [(0, 0)]
        while cnt < n + 1:
            cost, curr_house = heapq.heappop(pq)

            if in_mst[curr_house]:
                continue

            in_mst[curr_house] = True
            min_cost += cost
            cnt += 1

            for next_house, next_cost in graph[curr_house]:
                if not in_mst[next_house]:
                    heapq.heappush(pq, (next_cost, next_house))
        return min_cost
        