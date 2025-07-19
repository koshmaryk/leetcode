class Solution:
    '''
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]


        [0,0,0,0],
        [0,4,5,0],
        [0,3,1,0]

        [0,0,0,0],
        [0,4,5,2],
        [0,3,1,5]

    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(m):
            for c in range(n):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0