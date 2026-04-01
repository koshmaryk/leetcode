"""


456 012

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]