"""
[0,0,0]
[1,1,0]
[0,0,0]
[0,1,1]
[0,0,0]


"""
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])

        if k >= (R - 1 + C - 1):
            return (R - 1 + C - 1)

        queue = deque([(0, 0, k, 0)])

        state = (0, 0, k)
        visited = set([state])

        while queue:
            r, c, curr_k, steps = queue.popleft()

            if (r, c) == (R - 1, C - 1):
                return steps

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                new_k = curr_k - grid[nr][nc]
                state = (nr, nc, new_k)
                if new_k >= 0 and state not in visited:
                    queue.append((nr, nc, new_k, steps + 1))
                    visited.add(state)
        return -1