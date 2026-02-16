class Solution:
    '''

    k = 3
    0,1,0,3,0,12
    1,0,0,3,0,12
    1,3,0,0,0,12
    1,3,12,0,0,0


    '''
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = 0 # last non zero index
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        