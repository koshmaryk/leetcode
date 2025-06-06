class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 0
        #
        # 4, 5, 6, 7, 0, 1, 2
        # 
        # bad = 3, good = 7
        # 
        bad, good = -1, len(nums)
        while good - bad > 1:
            mid = (bad + good) // 2
            # left part is sorted
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    good = mid
                else:
                    bad = mid
            # right part is sorted
            else:
                if nums[mid] < target <= nums[-1]:
                    bad = mid
                else:
                    good = mid
        return good if good < len(nums) and nums[good] == target else -1