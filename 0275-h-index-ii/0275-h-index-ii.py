class Solution:
    '''
    0 1 2 3 4

    0,1,1,2,3,5,6

    n=7; 


    '''
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bad, good = -1, n
        while good - bad > 1:
            mid = (bad + good) // 2
            if citations[mid] >= n - mid:
                good = mid
            else:
                bad = mid
        return n - good