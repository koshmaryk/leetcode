class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
                
            memo[i] = max(robber(i + 1), robber(i + 2) + nums[i])
            return memo[i]
        
        memo = {}
        return robber(0)