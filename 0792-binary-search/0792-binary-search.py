class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 
        # -1,0,3,5,9,12
        #  0 1 2 3 4 5
        # bad = 1
        # good = 2
        bad = -1
        good = len(nums)
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[mid] >= target:
                good = mid
            else:
                bad = mid
        return good if good < len(nums) and nums[good] == target else -1
        