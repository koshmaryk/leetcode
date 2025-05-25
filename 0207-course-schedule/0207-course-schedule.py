from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        in_degrees = [0] * numCourses
        for course, prerequisite in prerequisites:
            G[prerequisite].append(course)
            in_degrees[course] += 1

        Q = []
        for u in range(numCourses):
            if in_degrees[u] == 0:
                heappush(Q, u)

        #ts = []
        visited = 0
        while Q:
            u = heappop(Q)
            #ts.append(u)
            visited += 1
            for v in G[u]:
                in_degrees[v] -= 1 # virtually remove u -> v
                if in_degrees[v] == 0:
                    heappush(Q, v)

        return visited == numCourses
        