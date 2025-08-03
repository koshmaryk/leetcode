class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i):
            if i < 2:
                return cost[i]

            if i in memo:
                return memo[i]

            memo[i] = min(helper(i - 1), helper(i - 2)) + cost[i]
            return memo[i]

        memo = {}
        return min(helper(len(cost) - 1), helper(len(cost) - 2))
        

# 10,15,20
#
# 10 20
# 15