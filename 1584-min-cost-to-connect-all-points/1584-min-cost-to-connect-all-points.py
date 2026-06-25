import heapq 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        pq = [(0, 0)] # weight, node (index)
        visited = [False] * n
        
        cost = cnt = 0
        while cnt < n:
            weight, node = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            cost += weight
            cnt += 1

            for next_node in range(n):
                if not visited[next_node]:
                    next_weight = abs(points[node][0] - points[next_node][0]) + abs(points[node][1] - points[next_node][1])

                    heapq.heappush(pq, (next_weight, next_node))
        return cost
