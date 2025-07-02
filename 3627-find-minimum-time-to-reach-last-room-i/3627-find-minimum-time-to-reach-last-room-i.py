class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            curr_dist, i, j = heapq.heappop(pq)
            visited[i][j] = 1

            for di,dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                    next_dist = max(dist[i][j], moveTime[ni][nj]) + 1
                    if next_dist < dist[ni][nj]:
                        dist[ni][nj] = next_dist
                        heapq.heappush(pq, (next_dist, ni, nj))
        return dist[n - 1][m - 1]
