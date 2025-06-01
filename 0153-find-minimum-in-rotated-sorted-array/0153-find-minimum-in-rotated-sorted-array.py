class Solution:
    def findMin(self, nums: List[int]) -> int:
        bad, good = -1, len(nums)
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] <= nums[-1]:
                good = mid
            else:
                bad = mid   
        return nums[good]