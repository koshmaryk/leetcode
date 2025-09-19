class Solution:
    '''
    time = [1,2,3], totalTrips 5

    3 // 3 = 1
    3 // 2 = 1
    3 // 1 = 3

    (0, max(time) * totalTrips + 1)
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)

        def isGoodEnough(total_time):
            trips = 0
            for t in time:
                trips += total_time // t
            return trips >= totalTrips

        bad, good = 0,  max(time) * totalTrips + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
        