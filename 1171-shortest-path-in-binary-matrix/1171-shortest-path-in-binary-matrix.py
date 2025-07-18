from collections import deque

'''
    [0,1,1,1,1,1,1,1],
    [0,1,1,0,0,0,0,0],
    [0,1,0,1,1,1,1,0],
    [0,1,0,1,1,1,1,0],
    [0,1,1,0,0,1,1,0],
    [0,1,1,1,1,0,1,0],
    [0,0,0,0,0,1,1,0],
    [1,1,1,1,1,1,1,0]

'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        queue = deque([(0, 0)])
        grid[0][0] = 1
        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
        return -1
