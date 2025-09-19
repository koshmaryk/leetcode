class Solution:
    '''
    bloomDay = [1,10,3,20,2], m = 3, k = 1


    [0, max(bloomDay)]


    '''
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        def isGoodEnough(days):
            bouquets = 0
            cnt = 0
            for day in bloomDay:
                if day <= days:
                    cnt += 1
                else:
                    cnt = 0
                    
                if cnt == k:
                    bouquets += 1
                    cnt = 0
            return bouquets >= m

        max_days = max(bloomDay)
        bad, good = 0, max_days + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good if good < max_days + 1 else -1
        