from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(R, C):
            queue = deque([(R, C)])
            board[R][C] = "E"

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                        board[nr][nc] = "E"
                        queue.append((nr, nc))

        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                    bfs(r, c)

        for r in range(m):
            for c in range(n):
                board[r][c] = "O" if board[r][c] == "E" else "X"

                    