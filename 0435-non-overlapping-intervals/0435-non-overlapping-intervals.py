class Solution:
    '''
    [[1,100],[11,22],[1,11],[2,12]]

    [[1,11],[2,12],[11,22],[1,100]]

    [[1,11],
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        curr_max = float('-inf')
        ans = 0

        for x, y in intervals:
            if x >= curr_max:
                curr_max = y
            else:
                ans += 1

        return ans