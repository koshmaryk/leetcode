class Solution:
    '''
        0 1 2 3
        4,7,9,10 k = 1

        4

    '''
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i - 1] - 1
            if gap >= k:
                return nums[i - 1] + k
            k -= gap
        return nums[-1] + k