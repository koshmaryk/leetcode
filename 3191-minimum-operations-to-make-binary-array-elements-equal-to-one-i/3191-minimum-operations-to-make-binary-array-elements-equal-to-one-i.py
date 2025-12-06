class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            if nums[i - 2] == 0:
                cnt = 2
                while cnt >= 0:
                    nums[i - cnt] ^= 1
                    cnt -= 1
                ans += 1

        if sum(nums) == len(nums):
            return ans
        return -1
        