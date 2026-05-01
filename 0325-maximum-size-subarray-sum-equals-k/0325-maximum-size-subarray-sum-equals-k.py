class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        seen = {0: -1}
        p = 0
        for i in range(n):
            p += nums[i]
            if p - k in seen:
                ans = max(ans, i - seen[p - k])

            if p not in seen:
                seen[p] = i

        return ans
            