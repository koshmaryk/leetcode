from math import inf


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)

        def count_ones(mask):
            cnt = 0
            while mask:
                mask &= (mask - 1)
                cnt += 1
            return cnt

        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])


        dp = [inf] * (1 << m)
        dp[0] = 0

        best = inf
        for mask in range(1 << m):
            i = count_ones(mask)
            if i >= n:
                best = min(best, dp[mask])
                continue

            for j in range(m):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + dist(i, j))
        return best