class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        ["X","X","X","X"]
        ["X","O","O","X"]
        ["X","O","O","X"]
        ["X","O","X","X"]

        ["X","X","X","X"]
        ["X","X","X","X"]
        ["X","X","X","X"]
        ["X","O","X","X"]
        """
        m, n = len(board), len(board[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def dfs(r, c, letter):
            board[r][c] = letter

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n) and (nr, nc) not in visited and board[nr][nc] != "X":
                    dfs(nr, nc, letter)

        
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                    dfs(r, c, "E")


        for i in range(m):
            print(board[i])

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    dfs(r, c, "X")
                elif board[r][c] == "E":
                    dfs(r, c, "O")

                    