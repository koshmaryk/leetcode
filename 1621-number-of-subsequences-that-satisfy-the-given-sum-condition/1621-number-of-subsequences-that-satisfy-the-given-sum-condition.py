class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        for l in range(len(nums)):
            if nums[l] * 2 > target:
                break

            bad, good = l, len(nums)
            while good - bad > 1:
                mid = (bad + good) // 2
                if nums[l] + nums[mid] > target:
                    good = mid
                else:
                    bad = mid
            
            ans += 2**(good - 1 - l)

        return ans % (10**9 + 7)