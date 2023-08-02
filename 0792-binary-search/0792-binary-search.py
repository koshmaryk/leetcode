class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bad = -1
        good = n
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] >= target:
                good = mid
            else:
                bad = mid

        if good == n or nums[good] != target:
            return -1
        else:
            return good