"""

k = 3

expected = 3

0,1,3,6,4,6,11

1,2,3,-2,2,5

3

{0:1, 1:1, 3:1, 6:1}




p[j] - p[i] = k
p[i] = p[j] - k

actual = 1

"""
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = defaultdict(int)
        count[0] = 1

        ans = 0
        p = 0
        for i in range(n):
            p += nums[i]
            if p - k in count:
                ans += count[p - k]

            count[p] += 1
        return ans
        