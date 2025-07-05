from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        ts = []
        queue = deque([v for v in range(numCourses) if in_degree[v] == 0])
        while queue:
            u = queue.popleft()
            ts.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return ts if len(ts) == numCourses else []