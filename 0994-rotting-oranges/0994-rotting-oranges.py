from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        EMPTY, FRESH, ROTTEN = 0, 1, 2
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        dist = [[float('inf')] * n for _ in range(m)]

        def bfs(row, col):
            visited = set([(row, col)])
            queue = deque([(row, col, 0)])
            while queue:
                r, c, d = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == FRESH:
                        dist[nr][nc] = min(dist[nr][nc], d + 1)
                        visited.add((nr, nc))
                        queue.append((nr, nc, d + 1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == ROTTEN:
                    bfs(r, c)

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == FRESH:
                    if dist[r][c] == float('inf'):
                        return -1

                    ans = max(ans, dist[r][c])
        return ans

