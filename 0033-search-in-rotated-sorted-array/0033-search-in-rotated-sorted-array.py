class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 0
        #
        # 4,5,6,7,0,1,2
        # 
        # 4,5,6,0,1,1,2
        # 
        # bad = -1, good = 7
        # 
        n = len(nums)
        bad, good = -1, n
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[0] <= nums[mid]:
                #  left is sorted
                if nums[0] <= target <= nums[mid]:
                    good = mid
                else:
                    bad = mid
            else:
                # right is sorted
                if nums[mid] < target <= nums[-1]:
                    bad = mid
                else:
                    good = mid
        return -1 if good == n or nums[good] != target else good