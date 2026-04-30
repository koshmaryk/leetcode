"""



    10,9,2,3,1,5,8

lis = 1,3,5,

dp[i] = 1 + max(dp[j] for all j < i and nums[j] < nums[i])

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [1] * n
        prev = [-1] * n
        idx = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > ans:
                ans = dp[i]
                idx = i

        lis = []
        while idx != -1:
            lis.append(nums[idx])
            idx = prev[idx]
        print(lis[::-1])
        return ans
        