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
        ans = lcounter[0] + rcounter[0]
        for i in range(n):
            d = k - nums[i]
            ans = max(ans, lcounter[d] + rcounter[-d])
            if i < n - 1:
                lcounter[diffs[i]] += 1
                rcounter[diffs[i]] -= 1
        return ans