class Solution:
    '''
        rows [0,0,0,0]
        cols [0,0,0]

        [1,1,2,0],
        [1,4,0,2],
        [1,3,1,5]

        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]

        [0,1,0,0],
        [0,4,0,2],
        [1,3,1,5]


        [0,0,0,0],
        [0,4,5,0],
        [0,3,1,0]

    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_col = False

        for r in range(m):
            if matrix[r][0] == 0:
                zero_col = True
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, 0, -1):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

            if zero_col:
                matrix[r][0] = 0
