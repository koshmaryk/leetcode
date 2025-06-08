class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                curr_length = 0
                while num + curr_length in s:
                    curr_length += 1
                ans = max(ans, curr_length)
        return ans

        # s = 100,4,200,1,3,2
        # 
        # nums = 100,4,200,1,3,2
        # 
        # ans = 4