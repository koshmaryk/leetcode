class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        for l in range(len(nums)):
            # nums[l] is the smallest possible value for nums[r], since r >= l
            if nums[l] * 2 > target:
                break

            bad, good = l, len(nums)
            while good - bad > 1:
                mid = (bad + good) // 2
                if nums[l] + nums[mid] > target:
                    good = mid
                else:
                    bad = mid
            
            ans += 2**(bad - l)

        return ans % (10**9 + 7)