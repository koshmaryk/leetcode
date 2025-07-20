class Solution:
    '''
        0 1 2 3  4  5  6
        4,7,9,10,12,13,15 k = 3

        nums[3] = 10

        10 - 4 = 6
        6 - 3 = 3
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
        