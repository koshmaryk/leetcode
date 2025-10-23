class Solution:
    '''
    [1, 5, 9 ]
    [10,11,13]
    [12,13,15]

    (0, 16)

    13

    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessOrEqual(num): # 13
            cnt = 0
            r, c = 0, n - 1 # 0,2 | 1,2 | 2,2 | 2,1 | 3,1
            while r < n and c >= 0:
                if matrix[r][c] <= num:
                    cnt += c + 1 # 0+3+3+2
                    r += 1
                else:
                    c -= 1
            return cnt

        n = len(matrix)
        bad, good = matrix[0][0] - 1, matrix[n - 1][n - 1] + 1 # 0,16 | 8,16 | 12,16 | 12,14 | 12,13
        while good - bad > 1:
            guess = (bad + good) // 2 # 8 | 12 | 14 | 13
            if countLessOrEqual(guess) >= k:
                good = guess
            else:
                bad = guess
        return good