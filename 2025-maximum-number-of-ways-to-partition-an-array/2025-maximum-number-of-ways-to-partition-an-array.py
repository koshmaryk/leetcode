"""
ans = 0

k = 3

nums 2,-1,2
diffs 1,-1,inf



"""
from collections import Counter

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diffs = []
        lsum, rsum = 0, sum(nums)
        for i in range(n - 1):
            lsum += nums[i]
            rsum -= nums[i]
            diffs.append(lsum - rsum)

        lcounter, rcounter = Counter(), Counter(diffs)
        ans = lcounter[0] + rcounter[0] # baseline
        for i in range(n):
            # changing nums[i] with k shifts every pivot's diff by delta
            # if i < pivot then (L + delta) - R; (L - R) + delta; old_diff + delta; 
            # valid if old_diff + delta = 0; old_diff = -delta
            # if i >= pivot then L - (R + delta); (L - R) - delta; old_diff - delta
            # valid if old_diff - delta = 0; old_diff = delta
            d = k - nums[i]
            ans = max(ans, lcounter[d] + rcounter[-d])

            if i < n - 1:
                lcounter[diffs[i]] += 1
                rcounter[diffs[i]] -= 1
        return ans