class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # rob1, rob2, nums[i], nums[i + 1], ... , nums[n - 1]
        for num in nums:
            rob1, rob2 = rob2, max(num + rob1, rob2)
        return rob2