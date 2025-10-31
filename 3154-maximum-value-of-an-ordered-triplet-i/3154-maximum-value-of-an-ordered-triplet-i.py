class Solution:
    '''
    maximize nums[i] in the interval [0,j)

    '''
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for k in range(2, n):
            maxi = nums[0]
            for j in range(1, k):
                ans = max(ans, (maxi - nums[j]) * nums[k])
                maxi = max(maxi, nums[j])
        return ans 