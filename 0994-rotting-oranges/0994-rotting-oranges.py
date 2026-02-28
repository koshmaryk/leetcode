from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        fresh_oranges = 0
        queue = deque([])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == FRESH:
                    fresh_oranges += 1
                if grid[r][c] == ROTTEN:
                    queue.append((r, c))

        t = -1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == FRESH:
                        fresh_oranges -= 1
                        grid[nr][nc] = ROTTEN
                        queue.append((nr, nc))
            t += 1
        return max(t, 0) if fresh_oranges == 0 else -1