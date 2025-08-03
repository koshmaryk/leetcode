class Solution:
    # 0 & n - 1; 1 & n
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robber(start, stop):
            rob1, rob2 = 0, 0

            for i in range(start, stop):
                rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
            return rob2

        return max(robber(0, n - 1), robber(1, n))
        