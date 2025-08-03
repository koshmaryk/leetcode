class Solution:
    # 0 & n - 1; 1 & n
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robber(start, stop):
            size = stop - start
            if size == 1:
                return nums[start]

            dp = [0] * size
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])

            for i in range(2, size):
                dp[i] = max(dp[i - 2] + nums[start + i], dp[i - 1])
            return dp[size - 1]

        return max(robber(0, n - 1), robber(1, n))
        