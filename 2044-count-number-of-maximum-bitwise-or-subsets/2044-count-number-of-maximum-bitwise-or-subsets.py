"""

index, curr_or

0 1 2 3
3,1,2,4

3,1 = 11
3   = 11

"""
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num

        memo = {}
        def dp(i, curr_or):
            if i == n:
                return 1 if curr_or == max_or else 0

            key = (i, curr_or)
            if key in memo:
                return memo[key]

            memo[key] = dp(i + 1, curr_or | nums[i]) + dp(i + 1, curr_or)
            return memo[key]

        return dp(0, 0)
