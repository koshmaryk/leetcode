"""

0123456
4560123

2

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        bad, good = -1, n
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] <= nums[-1]:
                good = mid
            else:
                bad = mid
        return nums[good]