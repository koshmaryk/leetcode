class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [1] * n
        for i in range(n):
            curr_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_max = max(curr_max, dp[j])
            dp[i] = 1 + curr_max
            ans = max(ans, dp[i])
        return ans
        