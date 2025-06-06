class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        bad, good = -1, m * n
        while good - bad > 1:
            mid = (bad + good) // 2
            if matrix[mid // n][mid % n] >= target:
                good = mid
            else:
                bad = mid
        if good < m * n and matrix[good // n][good % n] == target:
            return True
        else:
            return False
        