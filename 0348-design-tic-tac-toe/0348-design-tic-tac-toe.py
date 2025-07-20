class TicTacToe:
    '''
        2 1
        0 2

    '''
    def __init__(self, n: int):
        self.grid = [[0] * n for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.grid)
        self.grid[row][col] = player

        rows = 0
        for r in range(n):
            if self.grid[r][col] == player:
                rows += 1

        if rows == n:
            return player

        cols = 0
        for c in range(n):
            if self.grid[row][c] == player:
                cols += 1

        if cols == n:
            return player

        diagonal = 0
        r, c = 0, n -1
        while r < n and c >= 0:
            if self.grid[r][c] == player:
                diagonal += 1
            r += 1
            c -= 1

        if diagonal == n:
            return player

        diagonal = 0
        r, c = 0, 0
        while r < n and c < n:
            if self.grid[r][c] == player:
                diagonal += 1
            r += 1
            c += 1

        if diagonal == n:
            return player
            
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)