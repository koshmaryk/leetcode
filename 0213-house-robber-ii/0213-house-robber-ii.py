class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robber(houses):
            m = len(houses)
            rob1, rob2 = 0, 0
            for i in range(m):
                rob1, rob2 = rob2, max(rob2, rob1 + houses[i])
            return rob2
            
        return max(robber(nums[:-1]), robber(nums[1:]))