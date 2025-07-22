import heapq

'''
    capacity = 3
    [[2,1,5],[3,5,7]]

'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])

        pq = []
        total = 0
        for i in range(len(trips)):
            passengers, pickup, dropoff = trips[i]
            while pq and pq[0][0] <= pickup:
                total -= heapq.heappop(pq)[1]

            total += passengers
            if total > capacity:
                return False

            heapq.heappush(pq, (dropoff, passengers))

        return True
