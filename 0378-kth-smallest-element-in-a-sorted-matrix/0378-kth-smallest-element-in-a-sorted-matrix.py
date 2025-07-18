class Solution:
    '''
        [1, 5, 9 ],
        [10,11,13],
        [12,13,15]


        k = 2
        [1,4],
        [2,5]
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def countLessThanOrEqual(target: int): # 4
            count = 0 # 3
            r, c = 0, n - 1
            while r < n and c >= 0:
                if matrix[r][c] <= target:
                    count += (c + 1)
                    r += 1
                else:
                    c -= 1
            return count


        bad, good = matrix[0][0] - 1, matrix[n-1][n-1] + 1
        while good - bad > 1: # 5 | 4
            mid = (bad + good) // 2 # 1 | 1
            if countLessThanOrEqual(mid) >= k: # matrix[mid // n][mid % n]
                good = mid
            else:
                bad = mid
        return good #matrix[good // n][good % n]
        