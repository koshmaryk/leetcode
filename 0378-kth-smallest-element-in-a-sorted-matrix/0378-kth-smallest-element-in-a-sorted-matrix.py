import heapq

class Solution:
    '''
    [1, 5, 9 ]
    [10,11,13]
    [12,13,15]

    (0, 16)

    13

    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def isGoodEnough(target):
            cnt = 0
            r, c = 0, n - 1
            while r < n and c >= 0:
                if matrix[r][c] <= target:
                    cnt += c + 1
                    r += 1
                else:
                    c -= 1
            return cnt >= k

        bad, good = matrix[0][0] - 1, matrix[n - 1][n - 1]
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
