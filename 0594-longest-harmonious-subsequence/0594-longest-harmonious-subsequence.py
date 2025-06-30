class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        # 1,2,2,2,3,3,5,7
        # 1,1,2,2
        # l = 0, r = 3
        ans  = 0
        l = 0
        for r in range(0, len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1

            if nums[r] - nums[l] == 1:
                ans = max(ans, r - l + 1)
           
        return ans
