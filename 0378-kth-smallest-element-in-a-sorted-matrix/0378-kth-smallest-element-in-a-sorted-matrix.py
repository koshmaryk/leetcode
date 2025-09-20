import heapq

class Solution:
    '''
    [1, 5, 9 ]
    [10,11,13]
    [12,13,15]

    k = 8

    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []
        for r in range(min(k, n)):
            minHeap.append((matrix[r][0], r, 0))

        heapq.heapify(minHeap)

        ans = float('inf')
        for i in range(k):
            ans, r, c = heapq.heappop(minHeap)
            if c + 1 < n:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return ans

