class TicTacToe:
    '''
        2 1
        0 2

    '''
    def __init__(self, n: int):
        self.n = n
        self.grid = [[0] * n for _ in range(n)]
        
    def checkRow(self, col: int, player: int) -> bool:
        for r in range(self.n):
            if self.grid[r][col] != player:
                return False
        return True

    def checkCol(self, row: int, player: int) -> bool:
        for c in range(self.n):
            if self.grid[row][c] != player:
                return False
        return True

    def checkDiagonal(self, player: int) -> bool:
        for r in range(self.n):
            if self.grid[r][r] != player:
                return False
        return True

    def checkAntiDiagonal(self, player: int) -> bool:
        for r in range(self.n):
            if self.grid[r][self.n - r - 1] != player:
                return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = player

        if self.checkRow(col, player) or self.checkCol(row, player) or self.checkDiagonal(player) or self.checkAntiDiagonal(player):
            return player
            
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)