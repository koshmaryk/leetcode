from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)  
        ans = 0
        
        count = defaultdict(int)
        s = 0
        l = 0
        for r in range(n):
            s += nums[r]
            count[nums[r]] += 1

            if r - l + 1 > k:
                s -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            if r - l + 1 == k and len(count) == k:
                ans = max(ans, s)
        return ans