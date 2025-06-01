from collections import defaultdict
import heapq

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        G = defaultdict(list)
        for u, v, time in edges:
            if time > maxTime: continue
            G[u].append((v, time))
            G[v].append((u, time))

        times, costs = [float('inf')] * n, [float('inf')] * n
        times[0], costs[0] = 0, passingFees[0]
        pq = [(costs[0], times[0], 0)]
        heapq.heapify(pq)

        visited = set()
        while pq:
            ucost, utime, u = heapq.heappop(pq)

            if u == n - 1: return ucost

            # state = (u, utime)
            # if state in visited: continue
            # visited.add(state)

            for v, vtime in G[u]:
                new_time = utime + vtime
                new_cost = ucost + passingFees[v]

                if new_time > maxTime: continue

                if new_time < times[v] or new_cost < costs[v]:
                    times[v] = utime + vtime
                    costs[v] = ucost + passingFees[v]
                    heapq.heappush(pq, (costs[v], times[v], v))
        
        return -1 #if times[n - 1] > maxTime else costs[n - 1]
