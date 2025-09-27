class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        def isGoodEnough(h):
            cnt = 0
            for citation in citations:
                if citation >= h:
                    cnt += 1
            return cnt >= h

        bad, good = n, 0
        while bad - good > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return bad if isGoodEnough(bad) else good
