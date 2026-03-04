from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        ts = []
        colors = [-1] * numCourses
        def isCycle(u):
            if colors[u] == 0:
                return True
            if colors[u] == 1:
                return False

            colors[u] = 0
            for v in graph[u]:
                if isCycle(v):
                    return True
            colors[u] = 1
            ts.append(u)


        for u in range(numCourses):
            if colors[u] == -1:
                if isCycle(u):
                    return []
        ans = []
        while ts:
            ans.append(ts.pop())
        return ans
