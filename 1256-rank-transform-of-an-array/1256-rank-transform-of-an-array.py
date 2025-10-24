import heapq

class Solution:
    '''
    100 0, 100 1, 100 2

    '''
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)

        pq = []
        for i in range(n):
            pq.append((arr[i], i))

        heapq.heapify(pq)
        
        output = [0] * n
        rank = 0
        prev = float('inf')
        while pq:
            curr, idx = heapq.heappop(pq) # 100, 0

            if curr != prev:
                prev = curr
                rank += 1
            
            output[idx] = rank

        return output
