class Solution:
    # ans = 2, curr = 0, l = 1, r = 1, target = 4
    # ||
    # 1,4,4
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                ans = min(ans, r - l + 1)
                curr -= nums[l]
                l += 1
        return ans if ans < float('inf') else 0