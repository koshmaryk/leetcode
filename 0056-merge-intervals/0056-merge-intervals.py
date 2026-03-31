class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])

        merged = []
        for i in range(n):
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], intervals[i][1]))
        return merged