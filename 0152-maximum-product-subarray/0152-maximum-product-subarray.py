class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curr_min = curr_max = ans = nums[0]

        for i in range(1, n):
            candidates = [nums[i], curr_min * nums[i], curr_max * nums[i]]
            curr_min = min(candidates)
            curr_max = max(candidates)
            ans = max(ans, curr_max)
        return ans
