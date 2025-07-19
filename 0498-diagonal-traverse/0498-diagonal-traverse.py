class Solution:
    '''
        [1,2,4,7,5,3,6,8,9]

        [1,2,3],
        [4,5,6],
        [7,8,9]

        5
        0= 0,0; 1=0,1; 2=0,2; 3=1,2; 4=2,2

        0,0 0,0
        0,1 1,0
        2,0 0,2
        1,2 2,1
        2,2 2,2
    '''
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        m, n = len(mat), len(mat[0])
        arrow = 1
        r, c = 0, 0
        for i in range(m * n):
            output.append(mat[r][c])
            
            if (r + c) % 2 == 0:
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return output
        