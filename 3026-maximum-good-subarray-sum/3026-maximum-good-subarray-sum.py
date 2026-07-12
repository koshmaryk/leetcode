"""

sum(i..j) = p[j + 1] - p[i]
abs(nums[i] - nums[j]) == k

{nums[i]: sum(0..i-1)}

p1 - p2 (p before nums[i])

ans = 6
k = 1
-1,2,3,1

p = 5
{-1:0; 2:-1; 3:1; 1:4}

x-k
x+k
  
0,-1,1,4,5



"""
from math import inf


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = -inf

        min_p = {}
        p = 0
        for x in nums:
            if x not in min_p or min_p[x] > p:
                min_p[x] = p

            p += x

            if x - k in min_p:
                ans = max(ans, p - min_p[x - k])
            if x + k in min_p:
                ans = max(ans, p - min_p[x + k])
        
        return 0 if ans == -inf else ans
