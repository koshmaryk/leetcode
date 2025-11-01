class Solution:
    '''
    

    '''
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        if n == 2:
            return k * k

        two_back = k
        one_back = k * k

        for i in range(3, n + 1):
            curr = (k - 1) * (two_back + one_back)
            two_back, one_back = one_back, curr
        return one_back