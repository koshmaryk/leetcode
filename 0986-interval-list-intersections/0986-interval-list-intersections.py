"""

[[0,2],[5,10],[13,23],[24,25]]
[[1,5],[8,12],[15,24],[25,26]]

[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

[[0,2],[5,10]]
[[4,5],[8,12]]

l1 i
l2 j
max(start)
min(end)



"""
class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        output = []
        while i < len(l1) and j < len(l2):
            start = max(l1[i][0], l2[j][0])
            end = min(l1[i][1], l2[j][1])
            if start <= end:
                output.append([start, end])

            if l1[i][1] <= l2[j][1]:
                i += 1
            else:
                j += 1
        return output
        