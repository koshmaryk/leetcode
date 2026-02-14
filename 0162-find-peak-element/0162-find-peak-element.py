class Solution:
    '''

    5,2,3,4 => 0
    2,3,4,5 => 4
    2,3,1,0 => 1


    '''
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i
        return n - 1