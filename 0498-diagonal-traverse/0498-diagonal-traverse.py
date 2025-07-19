class Solution:
    '''
        [1,2,4,7,5,3,6,8,9]


        [1,2,3],
        [4,5,6],
        [7,8,9]


        5
        0= 0,0; 1=0,1; 2=0,2; 3=1,2; 4=2,2

    '''
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            diagonal = []

            r, c = 0 if i < n else i - n + 1, i if i < n else n - 1
            while r < m and c > -1:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1

            if i % 2 == 0:
                output.extend(diagonal[::-1])
            else:
                output.extend(diagonal)
        return output
        