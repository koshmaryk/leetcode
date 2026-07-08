from collections import defaultdict
import heapq
from math import inf


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for f,t,price in flights:
                if temp[f] < inf:
                    prices[t] = min(prices[t], temp[f] + price)
        return prices[dst] if prices[dst] < inf else -1
