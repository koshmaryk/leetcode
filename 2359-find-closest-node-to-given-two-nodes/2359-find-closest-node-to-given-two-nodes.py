class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def dfs(node, d, dist):
            dist[node] = d
            next_node = edges[node]
            if next_node != -1 and dist[next_node] == -1:
                dfs(next_node, d + 1, dist)


        dist1 = [-1] * n
        dfs(node1, 0, dist1)

        dist2 = [-1] * n
        dfs(node2, 0, dist2)

        ans, best = -1, float('inf')
        for node in range(n):
            if dist1[node] != -1 and dist2[node] != -1:
                d = max(dist1[node], dist2[node])
                if d < best:
                    best = d
                    ans = node
        return ans
