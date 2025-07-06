class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        perimeter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == 0:
                            perimeter += 1
        return perimeter