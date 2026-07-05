
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        visited = set()
        pq = [(0, 0, 0)]
        while pq:
            max_effort, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == m - 1 and c == n - 1:
                return max_effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in visited:
                    continue

                effort = abs(heights[r][c] - heights[nr][nc])
                heapq.heappush(pq, (max(max_effort, effort), nr, nc))
                
        return 0
