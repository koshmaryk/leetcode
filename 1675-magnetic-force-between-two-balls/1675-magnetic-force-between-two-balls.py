class Solution:
    '''
    positions = [1,2,3,4,7], m = 3




    '''
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)

        def isGoodEnough(force):
            balls = 1
            x = position[0]
            for i in range(1, n):
                y = position[i]
                if y - x >= force:
                    balls += 1
                    x = y
            return balls < m

        position.sort()

        bad, good = 0, position[-1] - position[0] + 1
        while good - bad > 1:
            guess = (bad + good) // 2
            if isGoodEnough(guess):
                good = guess
            else:
                bad = guess
        return bad
