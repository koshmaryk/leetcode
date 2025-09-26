class Solution:
    '''
    
    -2,-1,3,5,-1,2,4


    '''
    def maxSubArray(self, nums: List[int]) -> int:
        def findMaxSubArray(l, r):
            if l == r:
                return nums[l]

            mid = (l + r) // 2

            left_max = findMaxSubArray(l, mid)
            right_max = findMaxSubArray(mid + 1, r)

            left_sum = float("-inf")
            curr = 0
            for i in range(mid, l - 1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)

            right_sum = float("-inf")
            curr = 0
            for i in range(mid + 1, r + 1):
                curr += nums[i]
                right_sum = max(right_sum, curr)

            cross_sum = left_sum + right_sum
            
            return max(cross_sum, left_max, right_max)

        return findMaxSubArray(0, len(nums) - 1)
       