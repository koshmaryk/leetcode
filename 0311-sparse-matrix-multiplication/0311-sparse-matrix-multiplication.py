class Solution:
    '''

    [ 1,0,0]
    [-1,0,3]

    [7,0,0]
    [0,0,0]
    [0,0,1]

    '''
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M, K, N = len(mat1), len(mat1[0]), len(mat2[0])

        mat = [[0] * N for _ in range(M)]
        for i in range(M):
            for k in range(K):
                if mat1[i][k] == 0:
                    continue
                for j in range(N):
                    if mat2[k][j] == 0:
                        continue
                    mat[i][j] += mat1[i][k] * mat2[k][j]
        return mat
