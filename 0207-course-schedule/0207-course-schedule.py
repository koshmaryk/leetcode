from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        for course, prerequisite in prerequisites:
            G[prerequisite].append(course)

        # 0 - white, not visited; 1 - grey, visiting; 2 - black, visited
        state = [0] * numCourses
        def is_cycle(u):
            if state[u] == 1:
                return True
            if state[u] == 2:
                return False

            state[u] = 1
            for v in G[u]:
                if is_cycle(v):
                    return True
            state[u] = 2

        for u in range(numCourses):
            if state[u] == 0:
                if is_cycle(u):
                    return False
        return True