class Solution:
    '''
    k = 5

    0, 45

    22

    [1,2,3, 4,5, 6, 7, 8, 9]

    '''
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def isGoodEnough(total):
            cnt = 0
            curr = 0
            for s in sweetness:
                if curr + s > total:
                    cnt += 1
                    curr = 0
                else:
                    curr += s
            return cnt < k + 1


        bad, good = 0, sum(sweetness)
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return good
        