class Solution:
    '''
    maximize nums[i] in the interval [0,j)
    maximize nums[k] in the interval [j+1, n)

    [12,6,1,2,7]

    [0,12,12,12,12]
    [7,7,7,7,0]

    '''
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        imax, dmax = 0, 0
        for i in range(n):
            ans = max(ans, dmax * nums[i])
            imax = max(imax, nums[i])
            dmax = max(dmax, imax - nums[i])
        return ans 