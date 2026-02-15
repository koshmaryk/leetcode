from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)

        colors = [0] * numCourses

        def cycle(u):
            if colors[u] == 2:
                return False
            if colors[u] == 1:
                return True

            colors[u] = 1
            for v in graph[u]:
                if cycle(v):
                    return True
            colors[u] = 2
            return False

        for u in range(numCourses):
            if colors[u] == 0:
                if cycle(u):
                    return False
        return True
