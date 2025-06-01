from collections import defaultdict
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        G = defaultdict(list)
        for u, v, time in edges:
            if time > maxTime:
                continue
            G[u].append((v, time))
            G[v].append((u, time))

        times, costs = [float("inf")] * n, [float("inf")] * n
        times[0], costs[0] = 0, passingFees[0]
        pq = [(costs[0], times[0], 0)]
        heapq.heapify(pq)

        while pq:
            curr_cost, curr_time, city = heapq.heappop(pq)

            if city == n - 1:
                return curr_cost

            for next_city, travel_time in G[city]:
                new_cost = curr_cost + passingFees[next_city]
                new_time = curr_time + travel_time

                if new_time > maxTime:
                    continue

                if new_time < times[next_city] or new_cost < costs[next_city]:
                    costs[next_city] = new_cost
                    times[next_city] = new_time
                    heapq.heappush(pq, (new_cost, new_time, next_city))

        return -1