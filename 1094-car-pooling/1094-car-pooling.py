class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ts = [0] * 1001
        for passangers,pickup,dropoff in trips:
            ts[pickup] += passangers
            ts[dropoff] -= passangers
        
        total = 0
        for i in range(1001):
            total += ts[i]
            if total > capacity:
                return False
        return True
