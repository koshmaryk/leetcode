from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([])
        for u in range(numCourses):
            if indegree[u] == 0:
                queue.append(u)

        cnt = 0
        while queue:
            u = queue.popleft()
            cnt += 1

            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return cnt == numCourses
