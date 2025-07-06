class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        max_area = 0

        def dfs(r, c):
            if (r, c) in visited or not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0:
                return 0
            visited.add((r, c))

            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc     
                area += dfs(nr, nc)
            return area

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    max_area = max(max_area, curr_area)
        return max_area
