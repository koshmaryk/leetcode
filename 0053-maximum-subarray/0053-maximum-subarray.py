class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = float('-inf')
        curr = 0
        l = 0
        for r in range(n):
            curr += nums[r]
            ans = max(ans, curr)
            while curr < 0:
                curr -= nums[l]
                l += 1
        return ans
        