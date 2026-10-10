from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] += 1

        ans = 0
        p = 0 
        for num in nums:
            p += num
            if p - goal in count:
                ans += count[p - goal]
            count[p] += 1
        return ans
