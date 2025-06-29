class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += 2**(r - l) # l is min and any of [l+1, r] is max and can be included or excluded, so 2^(r - l)
                l += 1
            else:
                r -= 1
        return ans % (10**9 + 7)