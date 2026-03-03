"""
3,5; 10,12

0,1;
15,17;
7,9;

4,11 -> 3,12

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        bad, good = -1, len(intervals)
        while good - bad > 1:
            mid = (bad + good) // 2
            if intervals[mid][0] >= newInterval[0]:
                good = mid
            else:
                bad = mid

        intervals.insert(good, newInterval)

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
