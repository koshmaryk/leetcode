class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        ans = 0
        s = set(nums)
        for i in range(n):
            if nums[i] - 1 not in s:
                curr_length = 1
                while nums[i] + curr_length in s:
                    curr_length += 1
                ans = max(ans, curr_length)
        return ans
