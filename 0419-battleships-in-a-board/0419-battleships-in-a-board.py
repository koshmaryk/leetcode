class Solution:
    '''

    x..x
    ...x
    ...x

    '''
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        visited = set()


        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
           for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "X" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc)

        ans = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and board[r][c] == "X":
                    dfs(r, c)
                    ans += 1
        return ans
        