class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bad = -1
        good = len(nums)
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] >= target:
                good = mid
            else:
                bad = mid
        return good