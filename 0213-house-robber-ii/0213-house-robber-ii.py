class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robber(houses):
            m = len(houses)

            def helper(i):
                if i < 0:
                    return 0

                if i in memo:
                    return memo[i]
                
                memo[i] = max(helper(i - 1), helper(i - 2) + houses[i])
                return memo[i]

            memo = {}
            return helper(m - 1)
  
        return max(robber(nums[:-1]), robber(nums[1:]))