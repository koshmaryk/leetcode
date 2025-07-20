class Solution:
    '''
        1,1,1,0,0,0,1,1,1,1,0

      0,1,2,3,3,3,3,4,5,6,7,7 

    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        zeros = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        