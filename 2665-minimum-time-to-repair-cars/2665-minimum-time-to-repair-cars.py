import heapq
from collections import defaultdict

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        freq = defaultdict(int)
        for rank in ranks:
            freq[rank] += 1

        pq = []
        for rank in freq.keys():
            pq.append((rank, rank, 1, freq[rank]))
        heapq.heapify(pq)

        time = 0
        while cars > 0:
            next_time, rank, repaired, mechanics = heapq.heappop(pq)

            cars -= mechanics
            time = next_time
            repaired += 1

            heapq.heappush(pq, (rank * repaired ** 2, rank, repaired, mechanics))
        return time
        