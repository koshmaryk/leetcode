"""



    10,9,2,3,1,5,8

dp = 1,1,1,2,1,3,4

"""
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

            dp[i] = curr_max + 1
            ans = max(ans, dp[i])
        return ans
        