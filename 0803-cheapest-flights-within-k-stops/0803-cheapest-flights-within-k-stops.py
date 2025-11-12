from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        
        stops = [float('inf')] * n
        
        pq = [(0, 0, src)]
        
        while pq:
            price, stop, city = heapq.heappop(pq)
            
            if stop >= stops[city] or stop > k + 1:
                continue
            
            stops[city] = stop
            
            if city == dst:
                return price
            
            for next_city, next_price in graph[city]:
                heapq.heappush(pq, (price + next_price, stop + 1, next_city))
        
        return -1