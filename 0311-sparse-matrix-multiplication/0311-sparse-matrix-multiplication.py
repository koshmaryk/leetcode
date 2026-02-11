from collections import defaultdict

class Solution:
    '''

    [ 1,0,0]
    [-1,0,3]

    [7,0,0]
    [0,0,0]
    [0,0,1]

    s1 = {0: {0, 1}, 1: {0: -1, 2: 3}}
    s2 = {0: {0, 7}, 2: {2: 1}}

    '''
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M, K, N = len(mat1), len(mat1[0]), len(mat2[0])

        def to_sparse(mat):
            M, N = len(mat), len(mat[0])

            s = defaultdict(lambda: defaultdict(int))
            for i in range(M):
                for j in range(N):
                    if mat[i][j] != 0:
                        s[i][j] = mat[i][j]

            return s

        s1 = to_sparse(mat1)
        s2 = to_sparse(mat2)

        mat = [[0] * N for _ in range(M)]
        for i in range(M):
            if i in s1:
                for k in range(K):
                    if k in s1[i] and k in s2:
                        for j in range(N):
                            if j in s2[k]:
                                mat[i][j] += mat1[i][k] * mat2[k][j]
                    
        return mat
