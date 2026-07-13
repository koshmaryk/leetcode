"""

101
&
010
=
0

101
|
010
=
111



"""
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        bits = 0
        l = 0
        for r in range(n):
            while bits & nums[r] != 0:
                bits ^= nums[l]
                l += 1
            bits |= nums[r]
            ans = max(ans, r - l + 1)
        return ans