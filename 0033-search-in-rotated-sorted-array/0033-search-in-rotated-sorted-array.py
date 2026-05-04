"""
l mid r

which part is sorted, left or right?

0,1,2,3,4,5,6

4,5,6,7,0,1,2
|     |

4,5,6,0,1,1,2

target = 1
bad = -1, good = 7

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bad, good = -1, n
        while good - bad > 1:
            mid = (bad + good) // 2
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    good = mid
                else:
                    bad = mid
            else:
                if nums[mid] < target <= nums[-1]:
                    bad = mid
                else:
                    good = mid
        return -1 if good == n or nums[good] != target else good