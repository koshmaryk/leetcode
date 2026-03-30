import heapq

class Solution:
    '''
    [1,5,9]
    [10,11,13]
    [12,13,15]

    n = 3
    k = 2

    [1,7,8]
    [7,10,11]
    [8,11,12]

    min(k, n)

    [1,7,7,10,8,11]

    [1,7,7,8,10,11]

    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        for r in range(min(k, n)):
            pq.append((matrix[r][0], r, 0))

        heapq.heapify(pq)

        ans = None
        for i in range(k):
            element, r, c = heapq.heappop(pq)
            if c + 1 < n:
                heapq.heappush(pq, ((matrix[r][c + 1], r, c + 1)))
            ans = element
        return ans
        
