import heapq

'''
    capacity = 3
    [[2,1,5],[3,5,7]]

'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []
        for passengers, pickup, dropoff in trips:
            timestamps.append([pickup, passengers])
            timestamps.append([dropoff, -passengers])

        timestamps.sort()

        size = 0
        for location, passengers in timestamps:
            size += passengers
            if size > capacity:
                return False
        return True
