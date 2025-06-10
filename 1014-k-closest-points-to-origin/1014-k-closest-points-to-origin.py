import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x,y in points:
            dist = -(x**2 + y**2)**0.5
            heapq.heappush(pq, (dist, [x, y]))

            while len(pq) > k:
                heapq.heappop(pq)

        output = []
        while pq:
            _, cord = heapq.heappop(pq)
            output.append(cord)
        return output