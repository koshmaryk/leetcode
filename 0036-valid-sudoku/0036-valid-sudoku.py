class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in s:
                    return False

                s.add(board[i][j])

        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in s:
                    return False

                s.add(board[i][j])

        for square in range(9): # 5
            s = set()
            for i in range(3): # 1
                for j in range(3): # 1
                    row = (square // 3) * 3 + i # 4
                    col = (square % 3) * 3 + j # 7
                    if board[row][col] == ".":
                        continue

                    if board[row][col] in s:
                        return False

                    s.add(board[row][col])

        return True
        