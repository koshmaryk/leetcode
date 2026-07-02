class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)

        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        buckets = [[] for _ in range(2001)]
        for worker, (x1, y1) in enumerate(workers):
            for bike, (x2, y2) in enumerate(bikes):
                dist = distance(x1, y1, x2, y2)
                buckets[dist].append((worker, bike))

        bike_status = [False] * m
        answer = [-1] * n
        cnt = 0
        for bucket in buckets:
            for (worker, bike) in bucket:
                if answer[worker] == -1 and not bike_status[bike]:
                    bike_status[bike] = True
                    answer[worker] = bike
                    cnt += 1
                    if cnt == n:
                        break
        return answer
