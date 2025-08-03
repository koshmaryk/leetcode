class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robber(houses):
            m = len(houses)
            if m < 3:
                return max(houses)

            dp = [0] * m
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, m):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[-1]
            
        return max(robber(nums[:-1]), robber(nums[1:]))