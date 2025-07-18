import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        def estimate(r, c):
            return max(n - 1 - r, n - 1 - c)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        visited = set()
        pq = [(1 + estimate(0, 0), 1, 0, 0)]
        while pq:
            est, dist, r, c = heapq.heappop(pq)
            if (r, c) in visited:
                continue
            if r == n - 1 and c == n - 1:
                return dist

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    heapq.heappush(pq, (dist + 1 + estimate(nr, nc), dist + 1, nr, nc))
        return -1
