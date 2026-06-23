"""

k = 3

expected = 5

0,1,3,6,4,6,11

1,2,3,-2,2,3,5

3

{0:1, }



p[j] - p[i] = k
p[i] = p[j] - k

actual = 0

"""
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        counts = defaultdict(int)
        counts[0] = 1
        p = 0
        for num in nums:
            p += num
            ans += counts[p - k]
            counts[p] += 1
        return ans
        