"""
1,2,3,4,5
5,4,3,2,1

        1,2,3,5,4
asc     t t t t f
desc    f f f f t 

"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc, desc = True, True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                asc = False
            if nums[i] < nums[i + 1]:
                desc = False
        return asc or desc
