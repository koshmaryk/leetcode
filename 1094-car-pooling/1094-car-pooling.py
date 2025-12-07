class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ts = []
        for passangers,pickup,dropoff in trips:
            ts.append((pickup, passangers))
            ts.append((dropoff, -passangers))

        ts.sort()

        total = 0
        for i in range(len(ts)):
            total += ts[i][1]
            if total > capacity:
                return False
        return True