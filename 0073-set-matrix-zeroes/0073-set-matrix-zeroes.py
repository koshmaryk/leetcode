class Solution:
    '''
        [1,1,1],
        [1,0,1],
        [1,1,1]


        [1,0,0]
        [0,0,0]
        [0,0,0]

    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        zeros = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for i in range(m):
                        zeros.append((i, c))

                    for j in range(n):
                        zeros.append((r, j))
        
        for r, c in zeros:
            matrix[r][c] = 0