class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and 0 <= nr < n and 0 <= nc < m and grid[r][c] == '1':
                    visited.add((nr, nc))
                    dfs(nr, nc)

        n, m = len(grid), len(grid[0])
        count = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited and grid[r][c] == '1':
                    count += 1
                    visited.add((r, c))
                    dfs(r, c)

        return count
        