"""
x = 5

    1,1,4,2,3
  0,1,2,6,8,11

x = 4
    5,6, 7, 8, 9
  0,5,11,18,26,35

"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return n

        curr_s, longest = 0, -1
        l = 0
        for r in range(n):
            curr_s += nums[r]
            while curr_s > target:
                curr_s -= nums[l]
                l += 1

            if curr_s == target:
                longest = max(longest, r - l + 1)

        return -1 if longest == -1 else n - longest
