class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        ans = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                curr_length = 1
                while num + curr_length in s:
                    curr_length += 1
                ans = max(ans, curr_length)
        return ans
