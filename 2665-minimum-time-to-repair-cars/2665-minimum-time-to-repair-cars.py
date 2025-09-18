import heapq

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        pq = []
        for rank in ranks:
            pq.append((rank, rank, 1))
        heapq.heapify(pq)

        time = 0
        while cars > 0:
            next_time, rank, n = heapq.heappop(pq)

            cars -= 1
            time = next_time
            n += 1

            heapq.heappush(pq, (rank * n ** 2, rank, n))
        return time
        