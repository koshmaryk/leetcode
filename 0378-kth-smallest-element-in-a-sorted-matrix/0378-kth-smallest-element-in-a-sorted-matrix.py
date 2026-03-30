import heapq

class Solution:
    '''

    n = 3
    k = 2

    [1,7,8]
    [7,10,11]
    [8,11,12]

    [0,13]

    6,9,7

    bad=6
    good=7

    7

    min(k, n)

    ans = 7
    [7,10]

    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_less_or_equal(num):
            cnt = 0
            r, c = 0, n - 1
            while r < n and c >= 0:
                if matrix[r][c] <= num:
                    cnt += c + 1
                    r += 1
                else:
                    c -= 1
            return cnt

        bad, good = matrix[0][0] - 1, matrix[-1][-1] + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if count_less_or_equal(guess) >= k:
                good = guess
            else:
                bad = guess
        return good
