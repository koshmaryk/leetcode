import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)

        while len(pq) > k:
            heapq.heappop(pq)
        
        return pq[0]

        # 3,2,1,5,6,4
        # k = 2
        # 5,6
