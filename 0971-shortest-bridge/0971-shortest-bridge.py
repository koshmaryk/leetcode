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
        island = set()
        queue = deque([])

        def dfs(r, c):
            island.add((r, c))
            queue.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in island and grid[nr][nc] == 1:
                    dfs(nr, nc)

        i, j = 0, 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    i, j = r, c
                    break

        dfs(i, j)

        water = set()
        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                if (r, c) in water:
                    continue

                water.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if  0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1 and (nr, nc) not in island:
                            return distance

                        if grid[nr][nc] == 0:
                            queue.append((nr, nc))

            distance += 1
        return -1
