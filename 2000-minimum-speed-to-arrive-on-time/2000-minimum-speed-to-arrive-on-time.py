class Solution:
    '''
    dist = [1,3,2], hour = 2,7

    1/3
    '''
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        def isGoodEnough(speed):
            travel_time = 0
            for i in range(n):
                if i == n - 1:
                    travel_time += dist[i] / speed
                else:
                    travel_time += math.ceil(dist[i] / speed)
            return travel_time <= hour

        bad, good = 0, 10**7 + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return -1 if good == 10**7 + 1 else good
        