class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans, idx = 0, 0
        dp = [1] * n
        prev = [-1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > ans:
                ans = dp[i]
                idx = i

        path = [nums[idx]]
        while prev[idx] != -1:
            idx = prev[idx]
            path.append(nums[idx])
        print(path[::-1])

        return ans
        