from math import inf


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        used = [False] * m
        best_cost = inf


        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])


        def backtrack(i, curr_cost):
            nonlocal best_cost
            if curr_cost >= best_cost:
                return

            if i == n:
                best_cost = min(best_cost, curr_cost)
                return

            for j in range(m):
                if not used[j]:
                    used[j] = True
                    backtrack(i + 1, curr_cost + dist(i, j))
                    used[j] = False
        
        backtrack(0, 0)
        return best_cost
         