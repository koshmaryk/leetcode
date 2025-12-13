class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        [1,2,3] -> [1,3,2]

        [0,1,2,5,3,3,0] -> [0,1,3,5,3,2,0] -> [0,1,3,0,2,3,5]

        [3,2,1] -> [1,2,3]
        """
        n = len(nums)

        i = n - 1 # pivot
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i > 0:
            j = n - 1 # successor
            while nums[j] <= nums[i - 1]:
                j -= 1
                
            # swap pivot and successor
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # reverse suffix
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        
        
    