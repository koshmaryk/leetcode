class Solution:
    '''
        0 1 2 3  4 
        4,7,9,10,12 k = 3

        nums[mid] - nums[0] - mid >= k

        12-4-4 = 4

        4+3+1
    '''
    def missingElement(self, nums: List[int], k: int) -> int:
        bad, good = -1, len(nums)
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] - nums[0] - mid >= k:
                good = mid
            else:
                bad = mid
        return nums[0] + k + bad
        