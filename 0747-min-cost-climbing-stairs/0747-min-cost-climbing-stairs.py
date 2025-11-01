class Solution:
    '''
    dp[0] = cost[0]
    dp[1] = cost[1]
    dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    min(dp[n - 1], dp[n - 2])
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = {}
        
        def minCost(i):
            if i < 2:
                return cost[i]

            if i in memo:
                return memo[i]

            memo[i] = min(minCost(i - 1), minCost(i - 2)) + cost[i]
            return memo[i]

        return min(minCost(n - 1), minCost(n - 2))
        