class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0


    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if player == 1 else -1

        self.rows[row] += value
        if abs(self.rows[row]) == self.n:
            return player

        self.cols[col] += value
        if abs(self.cols[col]) == self.n:
            return player

        if row == col:
            self.diagonal += value
            if abs(self.diagonal) == self.n:
                return player
                
        if row == self.n - col - 1:
            self.anti_diagonal += value
            if abs(self.anti_diagonal) == self.n:
                return player
      
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)