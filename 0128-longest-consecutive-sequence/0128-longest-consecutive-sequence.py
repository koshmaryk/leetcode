class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                curr_len = 0
                while num + curr_len in s:
                    curr_len += 1
                ans = max(ans, curr_len)
        return ans
