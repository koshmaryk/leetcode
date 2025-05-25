from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            G[b].append(a) # prerequisite -> course
            in_degree[a] += 1

        Q = deque()
        for course_id in range(numCourses):
            if in_degree[course_id] == 0:
                Q.append(course_id)

        finished_courses = 0
        ts = []
        while Q:
            u = Q.popleft()
            finished_courses += 1
            ts.append(u)
            for v in G[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    Q.append(v)

        return finished_courses == numCourses #" ".join(map(str, ts))