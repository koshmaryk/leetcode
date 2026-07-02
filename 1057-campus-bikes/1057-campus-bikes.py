class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)

        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        pairs = []
        for worker, (x1, y1) in enumerate(workers):
            for bike, (x2, y2) in enumerate(bikes):
                pairs.append((distance(x1, y1, x2, y2), worker, bike))

        pairs.sort()
        
        bike_status = [False] * m
        answer = [-1] * n
        cnt = 0
        for _, worker, bike in pairs:
            if answer[worker] == -1 and not bike_status[bike]:
                bike_status[bike] = True
                answer[worker] = bike
                cnt += 1

            if cnt == n:
                break

        return answer
