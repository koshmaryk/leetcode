class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, ocean):
            ocean.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean)

        m, n = len(heights), len(heights[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        pacific, atlantic = set(), set()

        for r in range(m):
            dfs(r, 0, pacific)
        for c in range(n):
            dfs(0, c, pacific)

        for r in range(m):
            dfs(r, n - 1, atlantic)
        for c in range(n):
            dfs(m - 1, c, atlantic)

        return list(pacific.intersection(atlantic))