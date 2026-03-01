"""
    1 2 0 4
    0 3 1 5
    2 1 0 3

    1,3,3,4
    0,3,4,9
    2,3,3,6

    0,1 -> 0,3
    3,3 <- 3,1

    1 -> 1,1
    2 -> 2,2
    5

    1,1; 1,2; 2,2; 2,1

    for top-left until col from bottom-right
    for bottom-right until col from top-left


    top-left, -> right; bottom-right -> left

"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.p = [[0] * (n + 1) for _ in range(m)]
        for row in range(m):
            for col in range(n):
                self.p[row][col + 1] = self.p[row][col] + matrix[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            total += self.p[row][col2 + 1] - self.p[row][col1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)