class Solution:
    '''
    
    -2,-1,3,5,-1,2,4


    '''
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10**4
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            ans = max(ans, curr)
            while curr < 0:
                curr -= nums[l]
                l += 1
        return ans
