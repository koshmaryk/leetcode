import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        for r in range(n):
            for c in range(n):
                heapq.heappush(pq, -matrix[r][c])

                if len(pq) > k:
                    heapq.heappop(pq)
        return -heapq.heappop(pq)
        