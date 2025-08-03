class Solution:
    # 0 & n - 1; 1 & n
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robber(i, j):
            m = j - i
            if m == 1:
                return nums[i]

            dp = [0] * m
            dp[0] = nums[i]
            dp[1] = max(nums[i], nums[i + 1])

            for k in range(2, m):
                dp[k] = max(dp[k - 1], dp[k - 2] + nums[i + k])
            return dp[m - 1]

        return max(robber(0, n - 1), robber(1, n))
        