from collections import deque

class Solution:
    '''
        [0,1,0],
        [0,0,0],
        [0,0,1]

    '''
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        queue = deque([])

        def dfs(r, c):
            grid[r][c] = 2
            queue.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        i, j = 0, 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    i, j = r, c
                    break

        dfs(i, j)

        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if  0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance

                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1
                            queue.append((nr, nc))

            distance += 1
        return distance
