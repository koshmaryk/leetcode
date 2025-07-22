class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = [0] * 1001
        for passengers, pickup, dropoff in trips:
            timestamps[pickup] += passengers
            timestamps[dropoff] -= passengers

        total = 0
        for passengers in timestamps:
            total += passengers
            if total > capacity:
                return False
        return True