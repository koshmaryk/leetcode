class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = float('-inf')
        p = 0
        smallest_sum = 0
        for i in range(n):
            p += nums[i]
            ans = max(ans, p - smallest_sum)
            smallest_sum = min(smallest_sum, p)
        return ans
