"""

  5,4,-1,7,8

0,5,9,-1,7,8


3,4,-1,-4,7,8,-10

17

"""
from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        
        smallest = 0
        p = 0
        for x in nums:
            p += x
            ans = max(ans, p - smallest)
            smallest = min(smallest, p)
        return ans
