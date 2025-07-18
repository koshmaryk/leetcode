import heapq

class Solution:
    '''
        [1, 5, 9 ],
        [10,11,13],
        [12,13,15]

        pq = [13]
        k = 1
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        pq = []
        for r in range(min(k, n)):
            pq.append((matrix[r][0], r, 0))

        heapq.heapify(pq)

        element = pq[0][0]
        while k:
            element, r, c = heapq.heappop(pq)

            if c < n - 1:
                heapq.heappush(pq, (matrix[r][c + 1], r, c + 1))

            k -= 1

        return element
        
        # if x = min(k, n), then time complexity O(x log x) and space complexity O(x)