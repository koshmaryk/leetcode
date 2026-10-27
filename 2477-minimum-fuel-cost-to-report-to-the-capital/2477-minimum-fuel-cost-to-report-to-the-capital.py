"""
cities 0 .. n - 1
roads n - 1
capital 0
car in each city, seats = # of seats
1l of fuel to travel between any two cities

0-1-2-3

seats=5
min = 3

seats=1
min = 6

seats=2
min = 4

  3
  |
1-0-2

  0
  |
  1
 / \
2   3  


"""
from collections import defaultdict
import math

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)

        fuel = 0

        def dfs(node, parent):
            nonlocal fuel
            people = 1
            for next_node in graph[node]:
                if next_node != parent:
                    people += dfs(next_node, node)
            if node:
                fuel += math.ceil(people / seats)
            return people

        dfs(0, -1)
        return fuel
