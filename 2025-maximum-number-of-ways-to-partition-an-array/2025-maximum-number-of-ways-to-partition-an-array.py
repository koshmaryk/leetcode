class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        N = len(nums)
        diffs = []
        sl, sr = 0, sum(nums)
        for i in range(N - 1):
            sl += nums[i]
            sr -= nums[i]
            diffs.append(sl - sr)
        
        lcounter, rcounter = Counter(), Counter(diffs)
        ans = lcounter[0] + rcounter[0]
        for i in range(N):
            d = k - nums[i]
            ans = max(ans, lcounter[d] + rcounter[-d])
            if i < N - 1:
                lcounter[diffs[i]] += 1
                rcounter[diffs[i]] -= 1
        return ans