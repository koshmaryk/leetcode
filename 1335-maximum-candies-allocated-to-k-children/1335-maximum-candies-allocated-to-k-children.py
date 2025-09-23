class Solution:
    '''
    k = 3

    5,8,4,6

    5,5,3,5,1,4

    5,5,5 

    '''
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def count(x):
            cnt = 0
            for pile in candies:
                cnt += pile // x
            return cnt
        
        bad, good = max(candies) + 1, 0
        while bad - good > 1:
            guess = (bad + good) // 2
            if count(guess) >= k: 
                good = guess
            else:
                bad = guess
        return good
        