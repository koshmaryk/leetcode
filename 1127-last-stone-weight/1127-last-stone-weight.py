class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)

        while len(pq) > 1:
            y, x = -heapq.heappop(pq), -heapq.heappop(pq)
            z = y - x
            if z == 0:
                continue
            heapq.heappush(pq, -z)
        
        return -pq[0] if pq else 0