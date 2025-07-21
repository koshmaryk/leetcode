class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        bad, good = -1, len(nums)
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] > target:
                good = mid
            else:
                bad = mid
        
        if good <= len(nums) and nums[good - 1] != target:
            return [-1, -1]
        else:
            first, last = good - 1, good - 1
            while first > 0 and nums[first - 1] == target:
                first -= 1
          
            return [first, last]