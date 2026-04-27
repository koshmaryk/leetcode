class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        lsum = 0
        rsum = sum(nums)

        # [0, 10, 14, 6, 7]
        #  0   1   2  3  4 

        ans = 0
        for i in range(n - 1):
            lsum += nums[i]
            rsum -= nums[i]
            if lsum >= rsum:
                ans += 1
        return ans
