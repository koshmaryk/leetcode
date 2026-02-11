class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        R1, C1 = len(mat1), len(mat1[0])
        R2, C2 = len(mat2), len(mat2[0])

        mat = [[0] * C2 for _ in range(R1)]

        for i in range(R1):
            for k in range(C1):
                for j in range(C2):
                    mat[i][j] += mat1[i][k] * mat2[k][j]
        
        return mat        