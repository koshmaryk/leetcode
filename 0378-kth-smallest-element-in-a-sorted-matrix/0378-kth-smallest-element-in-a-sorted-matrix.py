import heapq

class Solution:
    '''
    [1, 5, 9 ]
    [10,11,13]
    [12,13,15]

    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        n = len(matrix)
        for r in range(n):
            for c in range(n):
                heapq.heappush(pq, -matrix[r][c])

                if len(pq) > k:
                    heapq.heappop(pq)
        return -pq[0]