class Solution:
    '''
        1,2,3,1


    '''
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        bad, good = -1, n - 1 # -1,3 | 1,3 | 1,2
        while good - bad > 1: # 4 | 2 | 1
            mid = (bad + good) // 2 # 1 | 2
            if nums[mid] > nums[mid + 1]: # 2 > 3 | 3 > 1
                good = mid
            else:
                bad = mid
        return good # 2