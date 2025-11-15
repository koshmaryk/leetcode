class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def find(r, c, i):
            if i == len(word):
                return True

            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i]:
                return False

            board[r][c] = "#"
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if find(nr, nc, i + 1):
                    board[r][c] = word[i]
                    return True

            board[r][c] = word[i]

            return False

        for r in range(m):
            for c in range(n):
                if find(r, c, 0):
                    return True
        return False
        