from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        # O(V)
        in_degrees = [0] * numCourses
        # O(E)
        for course, prerequisite in prerequisites:
            G[prerequisite].append(course)
            in_degrees[course] += 1

        Q = [] # min priority queue
        # O(V log V)
        for u in range(numCourses):
            if in_degrees[u] == 0:
                heappush(Q, u) # smaller id goes first

        visited = 0
        # O(V log V + E)
        while Q:
            u = heappop(Q)
            visited += 1
            for v in G[u]:
                in_degrees[v] -= 1 # virtually remove u -> v
                if in_degrees[v] == 0: # v is next candidate
                    heappush(Q, v) # smaller id goes first

        return visited == numCourses
        