class Solution:
    '''
    [[2,3],[4,5],[1,100]]

    [[2,3],[4,5],[1,100]]


    [[1,100],[11,22],[1,11],[2,12]]

    [[1,11],[2,12],[11,22],[1,100]]

    [[1,11],[2,12],[11,22],[1,100]]
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0

        intervals.sort(key = lambda x: x[1])
        
        t = float('-inf')
        for start,end in intervals:
            if start >= t:
                t = end
            else:
                ans += 1
        return ans