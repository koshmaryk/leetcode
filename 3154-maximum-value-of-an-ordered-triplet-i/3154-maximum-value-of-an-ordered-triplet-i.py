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
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i - 1])
            right[n - 1 - i] = max(right[n - i], nums[n - i])
            
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, (left[i] - nums[i]) * right[i])
        return ans 