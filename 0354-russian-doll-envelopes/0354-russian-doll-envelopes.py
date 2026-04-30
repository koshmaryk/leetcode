"""
1,2 | 1,3 | 1,4 | 2,3

1,4 | 1,3 | 1,2 | 2,3

"""
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))

        lis = []
        for w, h in envelopes:
            i = bisect.bisect_left(lis, h, key=lambda e: e[1])
            if i == len(lis):
                lis.append((w, h))
            else:
                lis[i] = (w, h)
        return len(lis)
