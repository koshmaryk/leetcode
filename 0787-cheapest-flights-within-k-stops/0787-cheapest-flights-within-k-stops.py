from collections import defaultdict
import heapq
from math import inf


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f,t,price in flights:
            graph[f].append((t, price))

        stops = [inf] * n
        pq = [(0, 0, src)]
        while pq:
            price, stop, city = heapq.heappop(pq)
            if city == dst:
                return price

            if stop >= stops[city] or stop > k:
                continue

            stops[city] = stop
            for next_city, next_price in graph[city]:
                heapq.heappush(pq, (price + next_price, stop + 1, next_city))
        return -1
