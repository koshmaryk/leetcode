class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bad = -1
        good = n
        
        while good - bad > 1:
            mid = (bad + good) // 2
            
            if nums[mid] == target:
                return mid
            
            # left half is sorted
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    # target is in the sorted left half
                    good = mid
                else:
                    # target is in the right half
                    bad = mid
            else: 
                # right half is sorted
                if nums[mid] < target <= nums[n-1]:
                    # target is in the sorted right half
                    bad = mid
                else:
                    # target is in the left half
                    good = mid
        
        return -1 # nums[good] if good < n and nums[good] == target else