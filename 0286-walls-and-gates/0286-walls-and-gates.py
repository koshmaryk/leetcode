from collections import deque

class Solution:
    '''
        3, -1, 0, 1
        2, 2, 1, -1
        1, -1, 2, -1
        0, -1, 3, 4

    '''
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        WALL, GATE, INF = -1, 0, 2**31 - 1
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        queue = deque([])
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == GATE:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n) or rooms[nr][nc] != INF:
                    continue

                rooms[nr][nc] = rooms[r][c] + 1

                queue.append((nr, nc))
