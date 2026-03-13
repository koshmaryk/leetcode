"""

[[0,2],[5,10],[13,23],[24,25]]
[[1,5],[8,12],[15,24],[25,26]]

[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

max(start1, start2)
min(end1, end2)

Keep max(end1, end2)?


"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                ans.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans
        