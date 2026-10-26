"""
012345
ababcc

0 2
1 3
4 5

0 3
4 5

4, 2


"""
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        intervals = {}
        for i, c in enumerate(s):
            if c not in intervals:
                intervals[c] = [i, i]
            else:
                intervals[c][1] = i
        
        sorted_intervals = sorted(intervals.values())
        merged = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            if start < merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        answer = []
        for start, end in merged:
            answer.append(end - start + 1)
        return answer
