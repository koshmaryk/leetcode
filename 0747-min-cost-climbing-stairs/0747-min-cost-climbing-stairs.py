class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(i):
            if i < 2:
                return cost[i]

            if i in memo:
                return memo[i]

            memo[i] = min(minCost(i - 1), minCost(i - 2)) + cost[i]
            return memo[i]

        memo = {}
        return min(minCost(len(cost) - 1), minCost(len(cost) - 2))
        

# 10,15,20
#
# 10 20
# 15