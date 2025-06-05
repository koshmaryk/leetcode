from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, price in flights:
            graph[f].append((t, price))

        dist = {}
        dist[(src, 0)] = 0

        pq = []
        heapq.heappush(pq, (0, src, 0))

        while pq:
            price, city, stops = heapq.heappop(pq)
            if city == dst:
                return price

            if stops > k:
                continue

            dist[(city, stops)] = price

            for next_city, next_price in graph[city]:
                new_price = price + next_price
                new_stops = stops + 1
                if (next_city, new_stops) not in dist or new_price < dist[(next_city, new_stops)]:
                    dist[(next_city, new_stops)] = new_price
                    heapq.heappush(pq, (new_price, next_city, new_stops))

        return -1
        