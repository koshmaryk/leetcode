class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]

        ans = 0
        for i in range(1, n):
            if p[i] >= p[n] - p[i]:
                ans += 1
        return ans
