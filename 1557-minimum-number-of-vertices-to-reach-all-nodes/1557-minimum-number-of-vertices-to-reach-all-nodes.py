class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _,t in edges:
            indegree[t] += 1

        return [node for node in range(n) if indegree[node] == 0]
