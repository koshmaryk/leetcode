"""
3,5; 10,12

0,1;
15,17;
7,9;
4,11

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                merged.append(newInterval)
                merged.extend(intervals[i:])
                return merged
            elif newInterval[0] > interval[1]:
                merged.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]
        merged.append(newInterval)
        return merged
