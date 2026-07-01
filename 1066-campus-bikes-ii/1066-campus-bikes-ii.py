from math import inf


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        memo = {}

        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])


        def dp(i, seen):
            if i == n:
                return 0

            if (i, seen) in memo:
                return memo[(i, seen)]
            
            best_cost = inf
            for j in range(m):
                if j not in seen:
                    best_cost = min(best_cost, dist(i, j) + dp(i + 1, seen | {j}))
            memo[(i, seen)] = best_cost
            return best_cost
        
        return dp(0, frozenset())
         