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
        flat = [0] * (n * n)
        for r in range(n):
            for c in range(n):
                flat[r * n + c] = matrix[r][c]

        flat.sort()
        return flat[k - 1]
