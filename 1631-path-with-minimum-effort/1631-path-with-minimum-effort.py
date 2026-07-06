from math import inf


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def can_reach(max_effort):
            visited = [[False] * n for _ in range(m)]

            def dfs(r, c):
                if r == m - 1 and c == n - 1:
                    return True

                visited[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        if abs(heights[r][c] - heights[nr][nc]) <= max_effort:
                            if dfs(nr, nc):
                                return True
                return False

            return dfs(0, 0)


        bad, good = -1, 1_000_001
        while good - bad > 1:
            mid = (bad + good) // 2
            if can_reach(mid):
                good = mid
            else:
                bad = mid
        return good