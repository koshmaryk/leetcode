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
from collections import defaultdict, deque
import math

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = defaultdict(list)
        degree = [0] * n
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        fuel = 0
        people = [1] * n
        q = deque([i for i in range(1, n) if degree[i] == 1])
        while q:
            node = q.popleft()
            fuel += math.ceil(people[node] / seats)
            for next_node in graph[node]:
                degree[next_node] -= 1
                people[next_node] += people[node]
                if degree[next_node] == 1 and next_node != 0:
                    q.append(next_node)
        return fuel
