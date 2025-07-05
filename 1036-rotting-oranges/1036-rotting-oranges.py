from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        orange = 0
        queue = deque([])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    orange += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        t = 0
        while orange > 0 and queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        orange -= 1
                        queue.append((nr, nc))
            t += 1

        return t if orange == 0 else -1